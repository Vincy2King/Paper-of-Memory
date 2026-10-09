# Beyond Sequences: Distilling Structured Decision Memory for LLM Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11501v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Leikun Liang, Guoshuai Wang, Xingsheng He, Yushan Han, Yunyi Xuan, Xiaoxiao Xu, Lin Qu
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.11501v1

## One-Sentence Summary
Despite the adoption of large language models (LLMs) in recommendation systems, prevailing approaches mostly model single-type behaviors (e.g., views or purchases).

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Despite the adoption of large language models (LLMs) in recommendation systems, prevailing approaches mostly model single-type behaviors (e.g., views or purchases).

进一步看，论文的核心做法或实验重点可以概括为：Even when incorporating multiple behaviors, existing methods flatten heterogeneous actions into homogeneous token sequences, ignoring their distinct decision-making roles.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Despite the adoption of large language models (LLMs) in recommendation systems, prevailing approaches mostly model single-type behaviors (e.g., views or purchases). Even when incorporating multiple behaviors, existing methods flatten heterogeneous actions into homogeneous token sequences, ignoring their distinct decision-making roles. This flattening fails to capture semantic hierarchies and contextual nuances in complex decision-making, such as trade-offs between price and quality. Consequently, performance degrades in critical ``difficult-choice'' scenarios involving highly similar items. To bridge this gap, we propose MARI (Memory-Augmented Recommendation with Interpretability), which grounds predictions in explicit, structured decision evidence. MARI maintains a Decision Memory Bank (DMB) that archives users' past rationales as Structured Decision Memories (SDMs): concise records of goals, constraints, and trade-offs. These SDMs are generated offline via Post-Hoc Decision Distillation from heterogeneous behaviors and user-generated content. By retrieving relevant SDMs to augment LLM reasoning, MARI achieves interpretability and scalability without the prohibitive cost of processing long raw sequences. Extensive experiments show MARI significantly outperforms state-of-the-art baselines on standard next-item prediction and a newly introduced Difficult Choice Prediction task, incurring low latency overhead by decoupling memory construction from online inference. Qualitative analyses reveal actionable, human-readable insights into user decision-making, marking a concrete step toward reasoning-aware recommendation systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
