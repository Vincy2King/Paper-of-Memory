# Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.00547v1
- Published: 2026-05-30
- Updated: 2026-05-30
- Authors: Yibo Wang, Nikki Lijing Kuang, Philip S. Yu, Zhewei Yao, Yuxiong He
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.00547v1

## One-Sentence Summary
Interactive text-to-SQL agents solve database tasks through multi-turn interactions involving schema exploration, query execution, feedback interpretation, and decision revision.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Interactive text-to-SQL agents solve database tasks through multi-turn interactions involving schema exploration, query execution, feedback interpretation, and decision revision.

进一步看，论文的核心做法或实验重点可以概括为：Long-term memory helps agents reuse past experiences, but existing retrieval methods remain limited.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval, retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Interactive text-to-SQL agents solve database tasks through multi-turn interactions involving schema exploration, query execution, feedback interpretation, and decision revision. Long-term memory helps agents reuse past experiences, but existing retrieval methods remain limited. Static methods rely on fixed similarity heuristics that do not optimize downstream utility, while dynamic methods often learn from sparse final outcomes and retrieve memories at a single decision horizon. This is insufficient when memory usefulness changes across interaction stages, since memories useful for initial planning may differ from those needed for local, state-conditioned execution. We propose MERIT, a dynamic multi-horizon memory retrieval framework. MERIT maintains episode-level memory for global strategic guidance and turn-level memory for local decision support. Both levels use learned retrieval policies optimized with reinforcement learning. To train turn-level retrieval despite limited intermediate supervision, MERIT uses a lightweight Process Reward Model to provide dense proxy rewards for local memory selection. Experiments on BIRD-Interact show that MERIT outperforms no-memory, static-retrieval, and dynamic-retrieval baselines in success rate while reducing average interaction turns. Transfer results on Spider2-Snow further show positive cross-benchmark transfer without benchmark-specific tuning. These results suggest that multi-horizon retrieval improves experience reuse in interactive text-to-SQL agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
