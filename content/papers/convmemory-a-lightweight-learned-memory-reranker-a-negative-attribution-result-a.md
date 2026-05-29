# ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.28062v1
- Published: 2026-05-27
- Updated: 2026-05-27
- Authors: Taiheng Pan
- Tags: benchmark, conversation, long-term, retrieval
- Categories: cs.CL, cs.IR
- URL: http://arxiv.org/abs/2605.28062v1

## One-Sentence Summary
We describe ConvMemory, a small 3.6M-parameter learned reranker for conversational long-term memory retrieval, trained with cross-encoder teacher supervision over fused dense...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We describe ConvMemory, a small 3.6M-parameter learned reranker for conversational long-term memory retrieval, trained with cross-encoder teacher supervision over fused dense and lexical features.

进一步看，论文的核心做法或实验重点可以概括为：On the LongMemEval memory family, ConvMemory operates above the BGE-large cross-encoder in Recall@10 at 12-47x lower latency, remains within 0.025 Recall@10 of mxbai-rerank-large-v1 on Clean500 while running 28x...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.CL, cs.IR

## Abstract Snapshot
We describe ConvMemory, a small 3.6M-parameter learned reranker for conversational long-term memory retrieval, trained with cross-encoder teacher supervision over fused dense and lexical features. On the LongMemEval memory family, ConvMemory operates above the BGE-large cross-encoder in Recall@10 at 12-47x lower latency, remains within 0.025 Recall@10 of mxbai-rerank-large-v1 on Clean500 while running 28x cheaper; under Stress1000 distractors the Recall@10 gap widens to 0.081 but ConvMemory still operates at 117x lower latency; these LongMemEval numbers are single-run or single-seed and are reported as indicative cost-frontier evidence, not benchmark-grade. We then publish a rigorous negative attribution result on a previously claimed mechanism: a five-seed retrained ablation with paired bootstrap shows that ConvMemory's learned temporal window is statistically significant on aggregate but not temporally specific, with the largest effects on hard non-temporal controls and no significant effect on multi-hop temporal queries. The honest description of the mechanism is cheap cross-encoder distillation in a fused dense+lexical feature space, not temporal-structure exploitation. We additionally release CCGE-LA, a low-amplitude conflict-aware candidate-set editor over ConvMemory, as a research preview with modest but consistent gains on supersession and stale/rescue slices on LoCoMo. All results are retrieval-stage; ConvMemory does not match mxbai-rerank-large-v1 in absolute LoCoMo MRR, and the report is single-author and not yet independently audited.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
