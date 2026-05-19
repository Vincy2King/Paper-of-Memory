# Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.17348v1
- Published: 2026-05-17
- Updated: 2026-05-17
- Authors: Taolin Zhang, Pukun Zhao, Qizhou Chen, Jiuheng Wan, Chen Chen, Xiaofeng He, Chengyu Wang, Richang Hong
- Tags: agent
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.17348v1

## One-Sentence Summary
Recent advancements in LLM-based multi-agent systems have demonstrated remarkable collaborative capabilities across complex tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advancements in LLM-based multi-agent systems have demonstrated remarkable collaborative capabilities across complex tasks.

进一步看，论文的核心做法或实验重点可以概括为：To improve overall efficiency, existing methods often rely on aggressive graph evolution among agents (e.g., node or edge pruning), which risks prematurely discarding valuable agents due to transient issues such as...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Recent advancements in LLM-based multi-agent systems have demonstrated remarkable collaborative capabilities across complex tasks. To improve overall efficiency, existing methods often rely on aggressive graph evolution among agents (e.g., node or edge pruning), which risks prematurely discarding valuable agents due to transient issues such as hallucinations or temporary knowledge gaps. However, such hard pruning overlooks the potential for ``zombie'' agents to recover and contribute in subsequent discussion rounds. In this paper, we propose AgentRevive, a Markov state-aware framework for resilient multi-agent evolution. Our approach dynamically manages agent collaboration through soft state transitions, implemented via two key components: (1) State-Aware Policy Learning: Agent states are divided into ``Active'', ``Standby'', and ``Terminated'' states, selectively propagating messages based on agent memory. The policy employs a risk estimator to optimize agent state transitions by assessing hallucination risk, minimizing the influence of unreliable nodes while safeguarding valuable ones. (2) State-Aware Edge Optimization: Subgraph edges are pruned according to states learned from the policy, permanently removing ``Terminated'' nodes and retaining ``Standby'' nodes for subsequent rounds to assess their potential future contributions. Extensive experiments on general reasoning, domain-specific, and hallucination challenge tasks show that our method consistently outperforms strong baselines and significantly reduces token consumption through state-aware agent scheduling.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
