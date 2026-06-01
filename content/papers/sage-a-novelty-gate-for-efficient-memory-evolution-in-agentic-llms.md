# SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30711v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Sijia Wang, Dhanajit Brahma, Ricardo Henao
- Tags: agent, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.LG, stat.ML
- URL: http://arxiv.org/abs/2605.30711v1

## One-Sentence Summary
Agentic LLMs must continuously decide whether newly extracted facts should be added, merged with existing memories, or ignored, yet prior work has focused more on retrieval and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic LLMs must continuously decide whether newly extracted facts should be added, merged with existing memories, or ignored, yet prior work has focused more on retrieval and storage than on principled write-side...

进一步看，论文的核心做法或实验重点可以概括为：We frame memory evolution as a novelty-detection problem and propose SAGE, a Spherical Adaptive Gate for memory Evolution that scores candidate facts with a von Mises-Fisher-based density estimator over memory...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.LG, stat.ML

## Abstract Snapshot
Agentic LLMs must continuously decide whether newly extracted facts should be added, merged with existing memories, or ignored, yet prior work has focused more on retrieval and storage than on principled write-side control. We frame memory evolution as a novelty-detection problem and propose SAGE, a Spherical Adaptive Gate for memory Evolution that scores candidate facts with a von Mises-Fisher-based density estimator over memory embeddings and routes them with an adaptive threshold that tracks memory-store geometry. SAGE resolves clearly novel facts as ADD, clearly redundant facts as NOOP, and sends only uncertain cases to an LLM merge step, reducing expensive write-time reasoning. On LoCoMo, SAGE achieves the best average token-F1 against Mem0 on all seven open-weight backbone comparisons, while on GPT-4o-mini it reduces add-phase API cost by 3.4$\times$ and add-phase latency by 2.5$\times$ with only a small average judge-score gap. As a drop-in binary gate for A-Mem, SAGE skips roughly 16-18% of LLM calls across five models with minimal quality change on open-weight backbones. These results suggest that novelty-aware write control is a practical lever for improving both memory quality and system efficiency in long-term agentic memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
