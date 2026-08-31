# LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.27809v1
- Published: 2026-08-28
- Updated: 2026-08-28
- Authors: Akito Hattori
- Tags: conversation, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.27809v1

## One-Sentence Summary
As an initial step toward personal memory retrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's...

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As an initial step toward personal memory retrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history.

进一步看，论文的核心做法或实验重点可以概括为：We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.IR

## Abstract Snapshot
As an initial step toward personal memory retrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history. We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt and other fixed text. We compared BM25, dense vector retrieval, and linear hybrid retrieval on 100 evaluation questions verified by a single annotator. Among individual retrievers, embedding_text_bm25 achieved the highest point estimate, with Recall@5 of 0.584. We then explored six retriever pairings and 21 weights, for 126 configurations on the same evaluation set. The selected combination of embedding_text_bm25 and embedding_text_vector at beta = 0.45 achieved Recall@5 = 0.697, MRR@5 = 0.595, and nDCG@5 = 0.575. Its Recall@5 exceeded that of embedding_text_bm25 by 0.113, with a question-level paired percentile-bootstrap 95% confidence interval of [0.048, 0.184]. This interval is conditional on fixing the configuration selected on the same 100 questions and does not account for uncertainty from configuration selection or weight search. The difference from a summary-based hybrid at beta = 0.50 was 0.050, with a 95% confidence interval of [-0.013, 0.115], so no clear difference could be established. The 17 aggregate questions also yielded lower point estimates than the other question types, suggesting that flat chunk-level retrieval struggles when evidence is distributed across multiple times and conversations. This evaluation is an exploratory single-user, single-annotator study conducted on the same question set used for configuration search; it does not evaluate final answer generation or generalization to unseen questions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
