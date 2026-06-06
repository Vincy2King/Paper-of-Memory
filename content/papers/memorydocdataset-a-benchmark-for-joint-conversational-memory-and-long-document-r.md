# MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04442v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Qiyang Xie, Jialun Wu, Xinjie He, Su Liu, Shuai Xiao, Zhiyuan Lin, Weikai Zhou
- Tags: benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.04442v1

## One-Sentence Summary
AI systems increasingly need to combine two demanding capabilities: navigating multi-session conversation history and performing deep reading comprehension within long documents.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI systems increasingly need to combine two demanding capabilities: navigating multi-session conversation history and performing deep reading comprehension within long documents.

进一步看，论文的核心做法或实验重点可以概括为：Yet no existing benchmark evaluates both simultaneously.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
AI systems increasingly need to combine two demanding capabilities: navigating multi-session conversation history and performing deep reading comprehension within long documents. Yet no existing benchmark evaluates both simultaneously. We introduce MemoryDocDataSet, a synthetic benchmark of 50 micro-worlds and 1,000 QA pairs in which each instance comprises 3-5 personas, a temporal event graph spanning months of activity, 3-5 real long documents (20,000-50,000 tokens each sourced from the Caselaw Access Project), multi-session conversations grounded on those documents, and 20 question-answer pairs across five reasoning categories. The defining feature is the Hybrid source tag: questions requiring a system to first navigate conversation history to identify which document is relevant, then extract the answer from within that document. Hybrid questions account for 75.1% of the dataset. Dataset quality is characterised through a prompt-sensitivity self-consistency analysis using LLM-as-judge, yielding a median Cohen's $κ= 0.634$ across all 50 micro-worlds. We evaluate six baseline configurations spanning truncated context, long-context LLMs, retrieval-augmented generation (RAG), and memory systems. The best baseline (RAG-Both) achieves 0.358 overall F1 and 0.342 on Hybrid. Document-only retrieval (RAG-Doc) collapses to 0.267 on Hybrid despite achieving 0.453 on Doc-only questions, demonstrating a clear joint-retrieval gap that motivates architectures unifying conversational memory with long-document navigation. We release the dataset, generation pipeline, and all baseline implementations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
