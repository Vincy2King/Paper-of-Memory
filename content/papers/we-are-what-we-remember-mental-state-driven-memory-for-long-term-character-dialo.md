# We Are What We Remember: Mental-State-Driven Memory for Long-Term Character Dialogue

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.16223v1
- Published: 2026-11-12
- Updated: 2026-11-12
- Authors: Zhicheng Jia, Shuchen Wu, Zhuoshi Tong, Haisen Liao, Sicheng Zhou
- Tags: agent, benchmark, context, conversation, episodic, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.16223v1

## One-Sentence Summary
Shared history in human dialogue is not merely a repository of facts, but the foundation of evolving relationships and mutual understanding.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Shared history in human dialogue is not merely a repository of facts, but the foundation of evolving relationships and mutual understanding.

进一步看，论文的核心做法或实验重点可以概括为：However, mainstream conversational memory systems rely on passive semantic similarity over external fact stores, frequently retrieving topically similar records while missing relationally pivotal experiences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, episodic, long-term
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Shared history in human dialogue is not merely a repository of facts, but the foundation of evolving relationships and mutual understanding. However, mainstream conversational memory systems rely on passive semantic similarity over external fact stores, frequently retrieving topically similar records while missing relationally pivotal experiences. Inspired by cognitive psychology's Self-Memory System (SMS), we propose MindMem, a mental-state-driven memory framework that asynchronously consolidates shared experiences into source-linked mental states of the character, the user, and their relationship. At each turn, a specialized mental-state reasoner (Mind) contextualizes these persistent states to anticipate latent user needs, form proactive intentions, and recover supporting episodic evidence that surface-level matching overlooks. To evaluate history-sensitive adaptation beyond factual recall, we introduce MemReal-Bench, a longitudinal benchmark grounded in month-long real-user interactions across dyadic and group scenes. By pairing Direct Question Answering (DQA) with Situated Memory Realization (SMR), it tests whether agents bridge the gap between knowing past facts and naturally using shared history, world rules, and relational trajectories. On MemReal-Bench, MindMem reaches 59.03% SMR and 82.58% DQA, exceeding the strongest memory baseline by 24.19 and 9.19 percentage points, respectively, and outperforming oracle target-memory injection on SMR. Code and dataset are available at https://github.com/jiazhicheng7-ctrl/MindMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
