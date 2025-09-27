<p align="center">
  <img src="assets/logo.png" width="200"/>
</p>

<h1 align="center">FinChain</h1>
<p align="center"><em>A Symbolic Benchmark for Verifiable Chain-of-Thought
Financial Reasoning</em></p>

<p align="center">
  <a href='https://arxiv.org/abs/2506.02515'><img src='https://img.shields.io/badge/paper-arXiv-red'></a> &nbsp;
  <a href='https://huggingface.co/spaces/Usmansafder/finchain-space'><img src='https://img.shields.io/badge/demo-Spaces-yellow'></a>
</p>

---

## 🔍 Overview

**FinChain** is the first benchmark designed for **verifiable chain-of-thought (CoT) financial reasoning**. It evaluates large language models on symbolic, multi-step problem-solving tasks grounded in financial equations. Built from scratch using a fine-grained financial taxonomy, FinChain enables step-level supervision and robust diagnostic evaluation.

> 📄 Paper: *FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought
Financial Reasoning* (EMNLP 2025 submission)

## 📚 Key Features

- **54 topics** across **12 financial domains**
- **5 symbolic templates per topic** (2 easy, 2 intermediate, 1 advanced)
- **Executable Python traces** for step-level answer verification
- **ChainEval**, a custom metric for evaluating both final answers and intermediate steps

## 🧠 Example Template

<p align="center">
  <img src="assets/example1.png" width="500"/>
</p>

This example shows a symbolic template for Compound Interest:
- Parameterized with named variables (e.g., `principal`, `rate`, `time`)
- Includes both natural language and step-by-step symbolic solution
- Fully executable and verifiable

## 🗂️ Dataset Structure

```
finchain/
├── data/
│   └── templates/        # Symbolic prompt templates for 54 financial topics
├── eval/                 # ChainEval evaluation scripts (coming soon)         
└── README.md
```

Each instance includes:
- A financial problem generated from symbolic templates
- Gold reasoning trace with intermediate variables and calculations
- Executable code for ground-truth generation and verification

## 🧭 Taxonomy of Domains and Topics

FinChain covers 54 financial topics across 12 domains:

<p align="center">
  <img src="assets/taxonomy.png" width="3000"/>
</p>

Domains include:
- Corporate Finance
- Investment Analysis
- Personal Finance
- Financial Ratios
- Risk Management
- Sustainable Finance
- Mergers & Acquisitions
- Financial Markets
- Fintech
- Crypto Finance
- Financial Reporting
- Finance Regulation

## 🧪 ChainEval Metric

FinChain introduces **ChainEval**, a joint evaluation framework for:
- ✅ **Final Answer Correctness (FAC)**
- 🔗 **Step Alignment** via:
  - Semantic similarity of reasoning steps
  - Numerical agreement at each step

This allows precise tracking of where models hallucinate, skip, or miscalculate.

## 📈 Benchmarking Results

We evaluate **30 models**, including:
- GPT-4.1, GPT-4o-mini, LLaMA 3.3 70B
- Qwen3, DeepSeek-R1, Mixtral, Mathstral
- Fin-tuned models: Fino1, FinR1, WiroAI Finance Qwen

**Findings:**
- Larger models outperform smaller financial-tuned models
- Even top models struggle on advanced templates and multi-hop symbolic chains
- FinChain reveals reasoning gaps not captured by standard accuracy metrics

## 🚀 Quick Start

```bash
git clone https://github.com/mbzuai-nlp/finchain.git
cd finchain
```

Explore templates:
```bash
ls data/templates/
```

Evaluate predictions (scripts coming soon):
```bash
python eval/eval_chain.py --pred path/to/your_outputs.jsonl
```

## 💬 Feedback & Contributions

**FinChain is an ongoing project**, and we’re continuously working to expand its coverage, refine evaluation metrics, and improve data quality. We **welcome feedback, suggestions, and community contributions**—whether it's about financial domains we missed, new evaluation ideas, or improving symbolic template diversity. If you're interested in collaborating or contributing, feel free to open an issue or contact us directly.

## 📄 Citation

If you find **FinChain** useful in your research, please consider citing our paper:

```bibtex

@article{xie2025finchain,
  title={FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning},
  author={Xie, Zhuohan and Sahnan, Dhruv and Banerjee, Debopriyo and Georgiev, Georgi and Thareja, Rushil and Madmoun, Hachem and Su, Jinyan and Singh, Aaryamonvikram and Wang, Yuxia and Xing, Rui and Koto, Fajri and Li, Haonan and Koychev, Ivan and Chakraborty, Tanmoy and Lahlou, Salem and Stoyanov, Veselin and Nakov, Preslav},
  journal={arXiv preprint arXiv:2506.02515},
  year={2025}
}


```


## 👥 Authors

FinChain is developed by:

Zhuohan Xie, Dhruv Sahnan, Debopriyo Banerjee, Georgi Georgiev,  
Rushil Thareja, Hachem Madmoun, Jinyan Su, Aaryamonvikram Singh,  
Yuxia Wang, Rui Xing, Fajri Koto, Haonan Li, Ivan Koychev,  
Tanmoy Chakraborty, Salem Lahlou, Veselin Stoyanov, Preslav Nakov

Affiliations: MBZUAI, Sofia University, Quantsquare, Cornell University, IIT Delhi

For questions or collaborations, contact: **zhuohan.xie@mbzuai.ac.ae**


## ⚖️ License


---

> **Disclaimer**: FinChain uses synthetic data based on symbolic financial equations. It does not reflect real-world financial advice or regulation.
