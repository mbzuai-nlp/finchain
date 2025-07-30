import random, torch
import re
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from langchain.schema import HumanMessage
import os
import pandas as pd
from tqdm import tqdm
from rouge_score import rouge_scorer
from bert_score import BERTScorer
import evaluate
import re
import warnings
 
from collections import Counter
import math
 
warnings.filterwarnings("ignore")
 
results_dir = '../results/'
evals_dir = '../evals/'
 
reasoning_models = [
    # List all files with model generations here
]
 
non_reasoning_models = [
    # List all files with model generations here
]
 
def load_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data
 
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
bertscorer = BERTScorer(model_type='allenai/longformer-base-4096', device='cuda' if torch.cuda.is_available() else 'cpu')
rougescorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)
 
def convert_to_float(text):
    # Remove non-numeric characters and convert to float
    # Extract numbers and handle special characters
    text = text.replace('~', '').strip()  # Remove approximate symbol
    text = text.replace('$', '').replace(',', '')  # Remove dollar sign and commas
    numbers = re.findall(r'[\d.]+', text)
    if not numbers:
        return None
   
    try:
        number = float(numbers[0])
    except:
        return None
 
    # Handle multipliers
 
    if 'billion' in text.lower():
        number *= 1000000000
    elif 'million' in text.lower():
        number *= 1000000
    elif 'thousand' in text.lower():
        number *= 1000
 
    return number
 
# Cos similarity on two bags of words over given threshold
def cos_similarity(a: str, b: str, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Pure cosine similarity between two raw strings (bag-of-words)."""
    c1, c2 = Counter(a.split()), Counter(b.split())
    vocab = set(c1) | set(c2)
    dot   = sum(c1[w] * c2[w] for w in vocab)
    n1    = math.sqrt(sum(c1[w] ** 2 for w in vocab))
    n2    = math.sqrt(sum(c2[w] ** 2 for w in vocab))
    val   = dot / (n1 * n2) if n1 and n2 else 0.0
    if val >= min_val and val <= max_val:
        return val
    return None
 
def extract_final_answer(step):
    # Replace all multiple spaces with a single space
    step = re.sub(r'\s+', ' ', step).strip()
 
    # Try capturing explicit "Answer: $" pattern
    answer_match = re.search(r'\**Answer:\**\s*.*?(?:USD|\$)?\s*([\d,]+(?:\.\d{1,2})?)', step)
    if answer_match:
        return convert_to_float(answer_match.group(0))
 
    # Fallback: last valid dollar-format number after =
    final_answer_match = re.search(r'=\s*(?!.*=)(?:USD|\$)?\s*[\d,]+(?:\.\d{1,2})?\s*(million|billion|thousand)?', step.lower())
    if final_answer_match:
        return convert_to_float(final_answer_match.group(0))
 
    # Fallback: last valid number in the step (Georgi)
    matches = list(re.finditer(r'\d+\.?[\d,]+(?:\.\d{1,2})?\s*(million|billion|thousand)?', step.lower()))
    if matches:
        last_number_match = matches[-1]
        return convert_to_float(last_number_match.group(0))
   
    # Fallback: extract last sentence (Georgi). Could start with "Answer: " or "Final Answer: " or "Final Answer is: " or \n or .
    last_sentence_match = re.search(r'(?<=\n|\.|:)\s*(answer: |final answer: |final answer is: )?([\d,]+(?:\.\d{1,2})?\s*(million|billion|thousand)?)', step.lower())
    if last_sentence_match:
        return last_sentence_match.group(0)
 
    return None
 
def extract_steps(text):
    if '\nuser\n' in text:
        text = text.split('\nuser\n')[0]
 
    # Find all instances of "Step" at the beginning of a line or after newline
    steps = re.finditer(r'(?:^|\n)(\s*)(\**)(#*)(\s*)Step(-*)(\s*)(\d+)', text)
    step_starts = [step.span()[0] for step in steps]
    if len(step_starts) == 0:
        steps = re.finditer(r'(?:^|\n)\s*(\**)(\d+)(.*)', text)
        step_starts = [step.span()[0] for step in steps]
    step_spans = [(step_starts[idx], step_starts[idx+1]) for idx in range(len(step_starts) - 1)]
 
    # Add the last step span
    if len(step_starts) > 0:
        step_spans.append((step_starts[-1], len(text)))
    step_strings = [text[start:end].strip() for start, end in step_spans]
 
    # Remove leading "Step X" from each step
    step_strings = [re.sub(r'(?i)Step\s+\d+\s*:', '', step).strip() for step in step_strings]
   
    # Find stepwise final answers
    step_final_answers = []
    for step in step_strings:
        # Find the last '=' and extract everything after it until the end
        step_final_answer = extract_final_answer(step)
        step_final_answers.append(step_final_answer)
 
    # Find final answer
    final_answer = None
    for step_final_answer in reversed(step_final_answers):
        if step_final_answer is not None:
            final_answer = step_final_answer
            break
 
    # Remove extra spaces
    step_strings = [re.sub(r'\s+', ' ', step) for step in step_strings]
 
    return step_strings, step_final_answers, final_answer
 
def preprocess_document(document):
    return re.sub(r"\s+", " ", document)
 
 
MAX_TOKENS = 4096  # Longformer's limit
 
def safe_score(bertscorer, gt, pred):
    if not isinstance(gt, str) or not isinstance(pred, str):
        print("Non-string input:", gt, pred)
        return 0.0
    if len(gt.strip()) == 0 or len(pred.strip()) == 0:
        print("Empty input:", gt, pred)
        return 0.0
 
    # Optional: truncate by tokens using the model's tokenizer
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("allenai/longformer-base-4096")
 
    gt_tokens = tokenizer(gt, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)
    pred_tokens = tokenizer(pred, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)
 
    try:
        # Re-decode to text after truncation (for BERTScore input)
        gt_truncated = tokenizer.batch_decode(gt_tokens["input_ids"], skip_special_tokens=True)[0]
        pred_truncated = tokenizer.batch_decode(pred_tokens["input_ids"], skip_special_tokens=True)[0]
        return bertscorer.score([gt_truncated], [pred_truncated])[2][0].item()
    except Exception as e:
        print("BERTScore error:", e)
        return 0.0
 
 
def evaluate_trace(gt, pred):
 
    if gt is None or pred is None:
        return None, None, None, None, None, None, None, None, None, None
 
    # Calculate Rouge scores
    rouge_score = rougescorer.score(gt, pred)
    rouge1, rouge2, rougeL, rougeLsum = rouge_score['rouge1'].fmeasure, rouge_score['rouge2'].fmeasure, rouge_score['rougeL'].fmeasure, rouge_score['rougeLsum'].fmeasure
 
    # Calculate BERTScore
    bert_score = safe_score(bertscorer, gt, pred)
 
    # Extract steps and final answers
    gt_steps, gt_step_final_answers, gt_final_answer = extract_steps(gt)
    pred_steps, pred_step_final_answers, pred_final_answer = extract_steps(pred)
 
    # If no steps or final answers, return zeros
    if len(gt_steps) == 0 or len(pred_steps) == 0:
        return 0, 0, 0, 0, rouge1, rouge2, rougeL, rougeLsum, bert_score
 
    # Convert steps to embeddings
    gt_steps_embeddings = model.encode(gt_steps)
    pred_steps_embeddings = model.encode(pred_steps)
 
    step_final_answer_correctness = [[0 for _ in range(len(pred_steps))] for _ in range(len(gt_steps))]
 
    for id_i, gt_step_answer in enumerate(gt_step_final_answers):
        if gt_step_answer is None:
            continue
        for id_j, pred_step_answer in enumerate(pred_step_final_answers):
            if pred_step_answer is None:
                continue
 
            # Handle string values
            if isinstance(gt_step_answer, str) or isinstance(pred_step_answer, str):
                # Calculate cosine similarity
                similarity = cos_similarity(str(gt_step_answer), str(pred_step_answer), min_val=0.5)
                if similarity is not None:
                    step_final_answer_correctness[id_i][id_j] = 1
                    break
 
            # Else handle numeric values
            elif abs(gt_step_answer - pred_step_answer) / (gt_step_answer + 0.0001) < 0.1:
                step_final_answer_correctness[id_i][id_j] = 1
                break
        else:
            step_final_answer_correctness[id_i][id_j] = 0
 
    # Calculate cosine similarity between step embeddings
    similarity_matrix = cosine_similarity(gt_steps_embeddings, pred_steps_embeddings)
    similarity_matrix = np.multiply(similarity_matrix, step_final_answer_correctness)
   
    # Calculate recall and precision
    max_similarities_backward = np.max(similarity_matrix, axis=1)
    max_similarities_forward = np.max(similarity_matrix, axis=0)
    binarized_similarity_backward = max_similarities_backward > 0.6
    binarized_similarity_forward = max_similarities_forward > 0.6
    recall = float(np.sum(binarized_similarity_backward) / len(gt_steps))
    precision = float(np.sum(binarized_similarity_forward) / len(pred_steps))
 
    # Check final answer match
    if gt_final_answer is None or pred_final_answer is None:
        final_answer_match = 0
   
    # Handle string values
    elif isinstance(gt_final_answer, str) or isinstance(pred_final_answer, str):
        # Calculate cosine similarity
        similarity = cos_similarity(str(gt_final_answer), str(pred_final_answer), min_val=0.1)
        final_answer_match = 1 if similarity is not None else 0
   
    # Else handle numeric values
    else:
        final_answer_match = int(abs(gt_final_answer - pred_final_answer)/(gt_final_answer + 0.0001) < 0.05)
 
    return recall, precision, final_answer_match, rouge2, rougeL, rougeLsum, bert_score
 
# Non-reasoning models
for model_file in os.listdir(f'{results_dir}'):
    if model_file.endswith('.jsonl'):
 
        if model_file not in non_reasoning_models:
            print(f"Skipping {model_file} for now.")
            continue
 
        with open(f'{evals_dir}{model_file}', 'w') as f_eval:
            with open(f'{results_dir}{model_file}', 'r') as f_pred:
                for line in tqdm(f_pred, desc=model_file, total=2700):
                   
                    json_line = json.loads(line)
                    recall, precision, final_answer_match, rouge2, rougeL, rougeLsum, bertscore = evaluate_trace(json_line['solution'], json_line['generation'])
 
                    result_json_line = {}
                    result_json_line['seed'] = json_line['seed']
                    result_json_line['id'] = json_line.get('id', None)
                    result_json_line['level'] = json_line['level']
                    result_json_line['topic'] = json_line['topic']
                    result_json_line['subtopic'] = json_line['subtopic']
                    result_json_line['model'] = json_line['model']
 
                    result_json_line['recall'] = recall
                    result_json_line['precision'] = precision
                    result_json_line['final_answer_match'] = final_answer_match
                    result_json_line['rouge2'] = rouge2
                    result_json_line['rougeL'] = rougeL
                    result_json_line['rougeLsum'] = rougeLsum
                    result_json_line['bertscore'] = bertscore
                    f_eval.write(json.dumps(result_json_line) + '\n')
 
print("Non-reasoning models evaluation completed.")
 
# ## Reasoning models
# for model_file in os.listdir(f'{results_dir}reasoning/'):
#     if model_file.endswith('.jsonl'):
 
#         if model_file not in reasoning_models:
#             print(f"Skipping {model_file} as it is not a reasoning model.")
#             continue
 
#         with open(f'{evals_dir}reasoning/{model_file}', 'w') as f_eval:
#             with open(f'{results_dir}reasoning/{model_file}', 'r') as f_pred:
#                 for line in tqdm(f_pred, desc=model_file, total=2700):
#                     json_line = json.loads(line)
#                     recall, precision, final_answer_match, rouge2, rougeL, rougeLsum, bertscore = evaluate_trace(json_line['solution'], json_line['generation_parsed'])
 
#                     result_json_line = {}
#                     result_json_line['seed'] = json_line['seed']
#                     result_json_line['id'] = json_line.get('id', None)
#                     result_json_line['level'] = json_line['level']
#                     result_json_line['topic'] = json_line['topic']
#                     result_json_line['subtopic'] = json_line['subtopic']
#                     result_json_line['model'] = json_line['model']
 
#                     result_json_line['recall'] = recall
#                     result_json_line['precision'] = precision
#                     result_json_line['final_answer_match'] = final_answer_match
#                     result_json_line['rouge2'] = rouge2
#                     result_json_line['rougeL'] = rougeL
#                     result_json_line['rougeLsum'] = rougeLsum
#                     result_json_line['bertscore'] = bertscore
#                     f_eval.write(json.dumps(result_json_line) + '\n')