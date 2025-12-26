import argparse
import json
import math
import re
import warnings
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import numpy as np
import torch
from bert_score import BERTScorer
from rouge_score import rouge_scorer as rouge_lib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity as pairwise_cosine
from tqdm import tqdm
from transformers import AutoTokenizer


warnings.filterwarnings("ignore")


DEFAULT_INPUT_PATH = Path(".")
DEFAULT_OUTPUT_PATH = Path("evals")
SENTENCE_EMBEDDER_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LONGFORMER_MODEL = "allenai/longformer-base-4096"
MAX_TOKENS = 4096  # tokenizer upper bound for Longformer
ALIGN_THRESHOLD = 0.45  # looser to avoid brittle zeros
VALUE_REL_TOL = 0.15
FINAL_REL_TOL = 0.05

# Soft DTW configuration
DTW_ALPHA_SIM = 0.85
DTW_BETA_NUM = 0.15
DTW_SIM_ACCEPT = 0.45
DTW_GAP_PENALTY = 0.25


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EMBEDDER = SentenceTransformer(SENTENCE_EMBEDDER_NAME)
BERT_EVALUATOR = BERTScorer(model_type=LONGFORMER_MODEL, device=DEVICE)
TOKENIZER = AutoTokenizer.from_pretrained(LONGFORMER_MODEL)
ROUGE = rouge_lib.RougeScorer(["rouge1", "rouge2", "rougeL", "rougeLsum"], use_stemmer=True)


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def bag_of_words_cosine(
    text_a: str, text_b: str, *, min_val: float = 0.0, max_val: float = 1.0
) -> Optional[float]:
    counts_a, counts_b = Counter(text_a.split()), Counter(text_b.split())
    vocab = set(counts_a) | set(counts_b)
    dot = sum(counts_a[token] * counts_b[token] for token in vocab)
    norm_a = math.sqrt(sum(counts_a[token] ** 2 for token in vocab))
    norm_b = math.sqrt(sum(counts_b[token] ** 2 for token in vocab))
    if not norm_a or not norm_b:
        return None
    similarity = dot / (norm_a * norm_b)
    if min_val <= similarity <= max_val:
        return similarity
    return None


def parse_numeric_value(text: str) -> Optional[float]:
    cleaned = text.replace("~", "").replace("$", "").replace(",", "").strip()
    matches = re.findall(r"[\d.]+", cleaned)
    if not matches:
        return None
    try:
        value = float(matches[0])
    except ValueError:
        return None

    lowered = text.lower()
    if "billion" in lowered:
        value *= 1_000_000_000
    elif "million" in lowered:
        value *= 1_000_000
    elif "thousand" in lowered:
        value *= 1_000
    return value


def extract_final_value(step_text: str) -> Optional[Any]:
    normalized = re.sub(r"\s+", " ", step_text).strip()

    patterns = [
        r"\**Answer:\**\s*.*?(?:USD|\$)?\s*([\d,]+(?:\.\d{1,2})?)",
        r"=\s*(?!.*=)(?:USD|\$)?\s*[\d,]+(?:\.\d{1,2})?\s*(million|billion|thousand)?",
        r"\d[\d,]+(?:\.\d{1,2})?\s*(million|billion|thousand)?",
        r"(?<=\n|\.|:)\s*(answer: |final answer: |final answer is: )?"
        r"([\d,]+(?:\.\d{1,2})?\s*(million|billion|thousand)?)",
    ]

    for pattern in patterns:
        matches = list(re.finditer(pattern, normalized.lower()))
        if matches:
            candidate = matches[-1].group(0)
            value = parse_numeric_value(candidate)
            return value if value is not None else candidate.strip()
    return None


def split_trace_into_steps(
    trace_text: Optional[str],
) -> Tuple[List[str], List[Optional[Any]], Optional[Any]]:
    if not isinstance(trace_text, str):
        return [], [], None

    content = trace_text.split("\nuser\n")[0] if "\nuser\n" in trace_text else trace_text
    step_matches = list(
        re.finditer(r"(?:^|\n)(\s*)(\**)(#*)(\s*)Step(-*)(\s*)(\d+)", content)
    )
    if not step_matches:
        step_matches = list(re.finditer(r"(?:^|\n)\s*(\**)(\d+)(.*)", content))
    if not step_matches:
        # Accept unnumbered "Step:" markers
        step_matches = list(re.finditer(r"(?:^|\n)(\s*)Step\s*:", content, re.IGNORECASE))

    if step_matches:
        indices = [match.span()[0] for match in step_matches]
        spans = [(indices[i], indices[i + 1]) for i in range(len(indices) - 1)]
        spans.append((indices[-1], len(content)))
        raw_steps = [content[start:end].strip() for start, end in spans]
    else:
        # Fallback: split by lines into coarse steps to avoid empty lists
        raw_steps = [ln.strip() for ln in content.splitlines() if ln.strip()]

    cleaned_steps = [re.sub(r"(?i)Step\s*\d*\s*:?", "", step).strip() for step in raw_steps]
    steps = [re.sub(r"\s+", " ", step) for step in cleaned_steps if step]

    values = [extract_final_value(step) for step in steps]
    final_value = next((value for value in reversed(values) if value is not None), None)
    return steps, values, final_value


def compute_bert_score(reference: Any, candidate: Any) -> float:
    if not isinstance(reference, str) or not isinstance(candidate, str):
        return 0.0
    if not reference.strip() or not candidate.strip():
        return 0.0

    ref_tokens = TOKENIZER(reference, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)
    cand_tokens = TOKENIZER(candidate, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)
    try:
        ref_text = TOKENIZER.batch_decode(ref_tokens["input_ids"], skip_special_tokens=True)[0]
        cand_text = TOKENIZER.batch_decode(cand_tokens["input_ids"], skip_special_tokens=True)[0]
        _, _, f1 = BERT_EVALUATOR.score([ref_text], [cand_text])
        return f1[0].item()
    except Exception:
        return 0.0


def build_value_match_mask(
    gold_values: List[Optional[Any]], pred_values: List[Optional[Any]]
) -> np.ndarray:
    mask = np.zeros((len(gold_values), len(pred_values)), dtype=float)
    for i, gold in enumerate(gold_values):
        if gold is None:
            mask[i, :] = 1.0  # allow text similarity when numeric missing
            continue
        for j, pred in enumerate(pred_values):
            if pred is None:
                mask[i, j] = 1.0
                continue
            if isinstance(gold, str) or isinstance(pred, str):
                if bag_of_words_cosine(str(gold), str(pred), min_val=0.3):
                    mask[i, j] = 1.0
            else:
                denominator = abs(gold) + 1e-4
                if abs(gold - pred) / denominator < VALUE_REL_TOL:
                    mask[i, j] = 1.0
    return mask


def score_trace(gold: Optional[str], pred: Optional[str]) -> Tuple[float, float, int, float, float, float, float]:
    if not isinstance(gold, str) or not isinstance(pred, str):
        return 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0

    rouge_scores = ROUGE.score(gold, pred)
    rouge2 = rouge_scores["rouge2"].fmeasure
    rouge_l = rouge_scores["rougeL"].fmeasure
    rouge_lsum = rouge_scores["rougeLsum"].fmeasure
    bert = compute_bert_score(gold, pred)

    gold_steps, gold_values, gold_final = split_trace_into_steps(gold)
    pred_steps, pred_values, pred_final = split_trace_into_steps(pred)
    if not gold_steps or not pred_steps:
        return 0.0, 0.0, 0, rouge2, rouge_l, rouge_lsum, bert

    gold_emb = EMBEDDER.encode(gold_steps)
    pred_emb = EMBEDDER.encode(pred_steps)
    sentence_sim = pairwise_cosine(gold_emb, pred_emb)

    mask = build_value_match_mask(gold_values, pred_values)
    masked_sim = np.multiply(sentence_sim, mask)

    recall = float(np.sum(np.max(masked_sim, axis=1) > ALIGN_THRESHOLD) / len(gold_steps))
    precision = float(np.sum(np.max(masked_sim, axis=0) > ALIGN_THRESHOLD) / len(pred_steps))

    if gold_final is None or pred_final is None:
        fam = 0
    elif isinstance(gold_final, str) or isinstance(pred_final, str):
        fam = 1 if bag_of_words_cosine(str(gold_final), str(pred_final), min_val=0.1) else 0
    else:
        fam = int(abs(gold_final - pred_final) / (abs(gold_final) + 1e-4) < FINAL_REL_TOL)

    return recall, precision, fam, rouge2, rouge_l, rouge_lsum, bert


def numeric_or_string_agree(a: Optional[Any], b: Optional[Any]) -> float:
    if a is None or b is None:
        return 1.0  # allow alignment to proceed on text when numbers missing
    if isinstance(a, str) or isinstance(b, str):
        return 1.0 if bag_of_words_cosine(str(a), str(b), min_val=0.3) else 0.0
    return 1.0 if abs(a - b) / (abs(a) + 1e-4) < VALUE_REL_TOL else 0.0


def build_similarity_and_bonus(
    gold_steps: List[str],
    pred_steps: List[str],
    gold_values: List[Optional[Any]],
    pred_values: List[Optional[Any]],
) -> Tuple[np.ndarray, np.ndarray]:
    if not gold_steps or not pred_steps:
        empty = np.zeros((len(gold_steps), len(pred_steps)))
        return empty, empty

    gold_emb = EMBEDDER.encode(gold_steps)
    pred_emb = EMBEDDER.encode(pred_steps)
    similarity = np.clip(pairwise_cosine(gold_emb, pred_emb), 0.0, 1.0)

    bonus = np.zeros_like(similarity)
    for i in range(len(gold_steps)):
        for j in range(len(pred_steps)):
            bonus[i, j] = numeric_or_string_agree(gold_values[i], pred_values[j])
    return similarity, bonus


def align_with_stats(cost: np.ndarray, gap_cost: float) -> Tuple[List[Tuple[int, int]], int, float]:
    n, m = cost.shape
    dp = np.full((n + 1, m + 1), np.inf, dtype=float)
    backtrack = np.zeros((n + 1, m + 1), dtype=int)
    dp[0, 0] = 0.0

    for i in range(1, n + 1):
        dp[i, 0] = dp[i - 1, 0] + gap_cost
        backtrack[i, 0] = 2
    for j in range(1, m + 1):
        dp[0, j] = dp[0, j - 1] + gap_cost
        backtrack[0, j] = 3

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            candidates = [
                dp[i - 1, j - 1] + cost[i - 1, j - 1],
                dp[i - 1, j] + gap_cost,
                dp[i, j - 1] + gap_cost,
            ]
            choice = int(np.argmin(candidates))
            dp[i, j] = candidates[choice]
            backtrack[i, j] = [1, 2, 3][choice]

    i, j = n, m
    path: List[Tuple[int, int]] = []
    path_len = 0
    while i > 0 or j > 0:
        move = backtrack[i, j]
        path_len += 1
        if move == 1:
            path.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif move == 2:
            i -= 1
        else:
            j -= 1
    path.reverse()
    return path, path_len, float(dp[n, m])


def dtw_metrics_from_score(
    score: np.ndarray, pairs: List[Tuple[int, int]], n_gold: int, n_pred: int
) -> Dict[str, float]:
    matched_gold = set()
    matched_pred = set()
    path_scores: List[float] = []

    for i, j in pairs:
        value = score[i, j]
        path_scores.append(value)
        if value >= DTW_SIM_ACCEPT:
            matched_gold.add(i)
            matched_pred.add(j)

    precision = len(matched_pred) / (n_pred + 1e-9)
    recall = len(matched_gold) / (n_gold + 1e-9)
    f1 = 0.0 if (precision + recall) == 0 else 2 * precision * recall / (precision + recall)
    avg_path_score = float(np.mean(path_scores)) if path_scores else 0.0
    return dict(
        precision=float(precision),
        recall=float(recall),
        f1=float(f1),
        avg_path_score=avg_path_score,
    )


def compute_dtw_metrics(gold: Optional[str], pred: Optional[str]) -> Dict[str, Dict[str, float]]:
    if not isinstance(gold, str) or not isinstance(pred, str):
        zero = dict(precision=0.0, recall=0.0, f1=0.0, avg_path_score=0.0, norm_score=0.0)
        return {"bonus": zero, "gate": zero}

    gold_steps, gold_values, _ = split_trace_into_steps(gold)
    pred_steps, pred_values, _ = split_trace_into_steps(pred)
    n, m = len(gold_steps), len(pred_steps)
    if n == 0 or m == 0:
        zero = dict(precision=0.0, recall=0.0, f1=0.0, avg_path_score=0.0, norm_score=0.0)
        return {"bonus": zero, "gate": zero}

    similarity, bonus = build_similarity_and_bonus(gold_steps, pred_steps, gold_values, pred_values)

    score_bonus = np.clip(DTW_ALPHA_SIM * similarity + DTW_BETA_NUM * bonus, 0.0, 1.0)
    cost_bonus = 1.0 - score_bonus
    pairs_bonus, len_bonus, total_cost_bonus = align_with_stats(cost_bonus, gap_cost=DTW_GAP_PENALTY)
    metrics_bonus = dtw_metrics_from_score(score_bonus, pairs_bonus, n, m)
    metrics_bonus["norm_score"] = float(1.0 - (total_cost_bonus / max(1, len_bonus)))

    score_gate = np.clip(np.multiply(similarity, bonus), 0.0, 1.0)
    cost_gate = 1.0 - score_gate
    pairs_gate, len_gate, total_cost_gate = align_with_stats(cost_gate, gap_cost=DTW_GAP_PENALTY)
    metrics_gate = dtw_metrics_from_score(score_gate, pairs_gate, n, m)
    metrics_gate["norm_score"] = float(1.0 - (total_cost_gate / max(1, len_gate)))

    return {"bonus": metrics_bonus, "gate": metrics_gate}


def build_result_record(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "seed": row.get("seed"),
        "id": row.get("id"),
        "level": row.get("level"),
        "topic": row.get("topic"),
        "subtopic": row.get("subtopic"),
        "model": row.get("model"),
    }


def evaluate_predictions_file(input_path: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as sink:
        for row in tqdm(read_jsonl(input_path), desc=input_path.name):
            metrics = build_result_record(row)

            recall, precision, fam, rouge2, rouge_l, rouge_lsum, bert = score_trace(
                row.get("solution"), row.get("model_generation")
            )
            dtw = compute_dtw_metrics(row.get("solution"), row.get("model_generation"))

            metrics.update(
                dict(
                    recall=recall,
                    precision=precision,
                    final_answer_match=fam,
                    rouge2=rouge2,
                    rougeL=rouge_l,
                    rougeLsum=rouge_lsum,
                    bertscore=bert,
                    dtw_precision_bonus=dtw["bonus"].get("precision", 0.0),
                    dtw_recall_bonus=dtw["bonus"].get("recall", 0.0),
                    dtw_f1_bonus=dtw["bonus"].get("f1", 0.0),
                    dtw_avg_path_score_bonus=dtw["bonus"].get("avg_path_score", 0.0),
                    dtw_norm_score_bonus=dtw["bonus"].get("norm_score", 0.0),
                    dtw_precision_gate=dtw["gate"].get("precision", 0.0),
                    dtw_recall_gate=dtw["gate"].get("recall", 0.0),
                    dtw_f1_gate=dtw["gate"].get("f1", 0.0),
                    dtw_avg_path_score_gate=dtw["gate"].get("avg_path_score", 0.0),
                    dtw_norm_score_gate=dtw["gate"].get("norm_score", 0.0),
                )
            )
            sink.write(json.dumps(metrics) + "\n")


def resolve_inputs(path: Path) -> List[Path]:
    if path.is_dir():
        return sorted(path.glob("*.jsonl"))
    if path.is_file() and path.suffix == ".jsonl":
        return [path]
    raise ValueError(f"No .jsonl files found for input path: {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate FinChain prediction traces.")
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to a .jsonl file or directory containing prediction files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Output directory where evaluation files will be written.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for input_file in resolve_inputs(args.input):
        output_file = args.output / input_file.name
        evaluate_predictions_file(input_file, output_file)


if __name__ == "__main__":
    main()
