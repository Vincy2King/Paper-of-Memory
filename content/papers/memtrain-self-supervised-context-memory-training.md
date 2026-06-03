# MemTrain: Self-Supervised Context Memory Training

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.03197v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Ziheng Li, Xingrun Xing, Haoqing Wang, Zhi-Hong Deng, Yehui Tang
- Tags: agent, benchmark, compression, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.03197v1

## One-Sentence Summary
Memory is an indispensable capability for long-horizon LLM agents, enabling them to preserve and utilize information accumulated across extended interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is an indispensable capability for long-horizon LLM agents, enabling them to preserve and utilize information accumulated across extended interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-agent approaches are typically trained end-to-end with reinforcement learning on downstream tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory is an indispensable capability for long-horizon LLM agents, enabling them to preserve and utilize information accumulated across extended interactions. Existing memory-agent approaches are typically trained end-to-end with reinforcement learning on downstream tasks. However, collecting high-quality annotated problems for memory-intensive scenarios is costly, and the resulting training data often lack sufficient diversity to cover general memory behaviors. In this work, we propose MemTrain, a self-supervised training framework for generally enhancing the context-memory capability of LLM agents for more effective downstream post-training. MemTrain introduces two coupled proxy tasks over unlabeled Wikipedia corpora: (1) an end-to-end masked reconstruction objective, which requires the model to recover masked entities after multiple rounds of memory updates, thereby encouraging memory maintenance from the final outcome perspective; and (2) an intermediate memory recall objective, which requires the model to reconstruct masked historical information using intermediate memory states, encouraging faithful compression and memory completeness throughout the interaction process. The two objectives are jointly optimized using GRPO. Extensive experiments on long-text QA and search-based QA benchmarks demonstrate that MemTrain consistently improves downstream memory-intensive reasoning performance across different models, achieving gains of up to 17.67 points over direct task-specific post-training.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
