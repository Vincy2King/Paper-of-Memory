# Training-Free Lexical-Dense Fusion for Conversational-Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04194v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Christian Lysenstøen
- Tags: conversation, long-term, retrieval
- Categories: cs.LG, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2606.04194v1

## One-Sentence Summary
Retrieving the few past turns that answer a new query across long multi-session histories is the retrieval bottleneck behind long-term conversational memory (LoCoMo, LongMemEval).

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieving the few past turns that answer a new query across long multi-session histories is the retrieval bottleneck behind long-term conversational memory (LoCoMo, LongMemEval).

进一步看，论文的核心做法或实验重点可以概括为：Recent concurrent work, Nano-Memory, shows that scoring a session by the maximum query-turn similarity (late interaction, "Turn Isolation Retrieval") beats mean-pooled session embeddings.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation, long-term, retrieval
- 检索关键词命中：conversational memory, memory retrieval
- 来源分类信息：cs.LG, cs.CL, cs.IR

## Abstract Snapshot
Retrieving the few past turns that answer a new query across long multi-session histories is the retrieval bottleneck behind long-term conversational memory (LoCoMo, LongMemEval). Recent concurrent work, Nano-Memory, shows that scoring a session by the maximum query-turn similarity (late interaction, "Turn Isolation Retrieval") beats mean-pooled session embeddings. We do not claim that effect; we replicate it and ask what a training-free, CPU-only retrieval stage should add around it. We report four findings. (1) Fuse: score-level fusion of the late-interaction dense score with BM25, under a single leave-one-conversation-out weight, adds +8.8 to +17.2 points of LoCoMo Hit@1 over late interaction alone across six encoders (all p<1e-4), reaching Hit@1 0.752 / NDCG@5 0.829 (e5-large-v2), +11.2 pp over BM25. (2) An off-the-shelf web-search cross-encoder reranker over the fused top-10 hurts here, degrading Hit@1 by 6.9 pp (one reranker, one configuration). (3) A pooling-operator ablation shows top-k late interaction matches max-similarity, but a naive smooth-max (log-sum-exp) collapses for half the encoders. (4) The late-minus-early gap is large for all six encoders and tends to be larger for larger ones, while the marginal fusion gain shrinks; on LongMemEval-S, a lexical regime where BM25 saturates, the net fusion gain over BM25 is small and not significant. A per-category analysis frames the gain as a division of labor: dense late interaction helps most on multi-hop and temporal questions but trails BM25 on adversarial ones. The contribution is a controlled, reproducible account of a strong training-free retrieval recipe, not the late-interaction retriever itself (Nano-Memory's). We make no claim to a complete memory architecture; this is a retrieval-stage study.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
