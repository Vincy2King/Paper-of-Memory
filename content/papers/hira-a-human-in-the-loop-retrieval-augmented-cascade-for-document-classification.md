# HIRA: A Human-in-the-Loop Retrieval-Augmented Cascade for Document Classification in Regulated Industries

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.21792v1
- Published: 2026-08-22
- Updated: 2026-08-22
- Authors: Shangxuan Tian, Yanhui Chen, Carlos Queiroz
- Tags: benchmark, retrieval
- Categories: cs.AI, cs.CV, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2608.21792v1

## One-Sentence Summary
Document classification in regulated industries is constrained by data residency, limited cold-start labels, scarce review capacity, and costly model-governance procedures.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Document classification in regulated industries is constrained by data residency, limited cold-start labels, scarce review capacity, and costly model-governance procedures.

进一步看，论文的核心做法或实验重点可以概括为：We present HIRA, a training-free, on-premises retrieval-augmented cascade for document classification in regulated deployments that combines BM25 over OCR text, dense text embeddings, and image-level representations...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI, cs.CV, cs.IR, cs.LG

## Abstract Snapshot
Document classification in regulated industries is constrained by data residency, limited cold-start labels, scarce review capacity, and costly model-governance procedures. We present HIRA, a training-free, on-premises retrieval-augmented cascade for document classification in regulated deployments that combines BM25 over OCR text, dense text embeddings, and image-level representations through validation-calibrated weighted reciprocal-rank fusion. Confident documents are classified directly by retrieval; uncertain or visually confusable documents are passed to a locally hosted LLM verifier, which receives the OCR text, retrieved exemplars, label descriptions, and confusion-specific terms. When the verifier remains uncertain, the document is sent to human review. Each correction is stored as a margin-weighted retrieval exemplar and updates a Dirichlet-smoothed confusion graph, letting the system improve without updating model weights. On a private 80-class trade-finance corpus, HIRA processes the full 30,233-document production stream while requesting human correction for only 1,945 documents (6.4%), improving Macro-F1 from 0.6218 to 0.8548. On the corrected Tobacco-3482 benchmark, HIRA reaches 0.9423 Macro-F1 with a locally hosted DeepSeek-R1-Distill-Qwen-32B verifier, 17.4 percentage points above the zero-shot LLM baseline, while invoking the verifier for only about 40% of documents and reducing LLM calls by approximately 60%. With 518 human corrections (24.8% of the pool), HIRA matches the fully labelled pool oracle, in which all 2,086 pool documents are indexed with their ground-truth labels. These results show that selective human feedback and retrieval-memory adaptation can be a practical alternative to repeated model retraining for long-tail document classification in regulated deployments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
