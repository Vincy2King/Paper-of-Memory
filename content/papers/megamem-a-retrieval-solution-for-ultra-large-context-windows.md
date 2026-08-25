# MegaMem: A Retrieval Solution for Ultra-Large Context Windows

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22137v1
- Published: 2026-08-22
- Updated: 2026-08-22
- Authors: Xinyuan Song, Bowen Zhu, Hasibul Haque, Liang Zhao
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.22137v1

## One-Sentence Summary
Modern language models and agents increasingly require persistent memory for complete codebases, long interaction histories, and heterogeneous enterprise records.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modern language models and agents increasingly require persistent memory for complete codebases, long interaction histories, and heterogeneous enterprise records.

进一步看，论文的核心做法或实验重点可以概括为：The key challenge is to keep hundreds of millions of tokens searchable while passing only bounded source evidence to the answer model.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Modern language models and agents increasingly require persistent memory for complete codebases, long interaction histories, and heterogeneous enterprise records. The key challenge is to keep hundreds of millions of tokens searchable while passing only bounded source evidence to the answer model. We introduce MegaMem, a source-resolved dual-view retrieval system that separates semantic access from generation evidence. Distilled records and detailed evidence are searched with original and transformed queries; every distilled hit resolves to an immutable source ID before reciprocal-rank fusion, deduplication, and cross-encoder reranking; and only the highest-ranked detailed evidence within a fixed budget supports generation. Post-answer attribution then identifies which loaded sources support the fixed answer. We evaluate MegaMem on EnterpriseRAG-Bench, which contains more than 500,000 heterogeneous enterprise documents and approximately 650M tokens. MegaMem improves Overall from 68.22 to 82.26 and reaches 86.50 Correctness. These results show that MegaMem supports ultra-large persistent memory while preserving strong answer accuracy under a bounded generation context. By separating searchable memory scale from answer-context size, MegaMem provides a practical path toward accurate retrieval over memories ranging from hundreds of millions to one billion tokens. Our code is available at https://github.com/ xfab-xinyuansong/MegaMem.git.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
