# All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21147v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Bingbing Wang, Jingjie Lin, Weiming Qiao, Jing Li, Ruifeng Xu
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.21147v1

## One-Sentence Summary
Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory methods often optimize retrieval and memory construction separately, without a shared reward space for evaluating search, writing, and stopping decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：context memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents. However, existing memory methods often optimize retrieval and memory construction separately, without a shared reward space for evaluating search, writing, and stopping decisions. To address this, we propose All-in-One Memory (AiO-Mem), which organizes these operations as transitions over a shared evidence state and directly evaluates the semantic quality of each action in a unified reward space. AiO-Mem compiles heterogeneous histories into source-traceable multi-view events, providing a shared substrate for retrieval and memory writing. A unified memory policy actor then rolls out complete interaction trajectories over this shared evidence state. A separate trajectory-conditioned process reward model is trained through evidence-grounded supervised fine-tuning and trajectory-level DPO to assign process scores to the collected trajectories. These scores are aggregated into an action-balanced trajectory reward and used by Process-Aligned DAPO (PA-DAPO) to optimize the memory policy. Across long-context memory benchmarks, AiO-Mem consistently improves answer accuracy over both static memory systems and RL-trained memory agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
