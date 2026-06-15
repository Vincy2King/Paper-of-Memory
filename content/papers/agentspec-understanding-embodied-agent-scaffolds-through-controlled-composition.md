# AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.14674v1
- Published: 2026-06-12
- Updated: 2026-06-12
- Authors: Jixuan Chen, Jianzhi Shen, Haoqiang Kang, Zhi Hong, Qingyi Jiang, Soham Bose, Yiming Zhang, Leon Leng, Amit Vyas, Lingjun Mao, Siru Ouyang, Kun Zhou, Lianhui Qin
- Tags: agent
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.14674v1

## One-Sentence Summary
LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning.

进一步看，论文的核心做法或实验重点可以概括为：While such scaffolds often improve performance, they are often embedded in tightly coupled pipelines, making it difficult to isolate component contributions, compare alternative designs, or understand how module...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.CL

## Abstract Snapshot
LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning. While such scaffolds often improve performance, they are often embedded in tightly coupled pipelines, making it difficult to isolate component contributions, compare alternative designs, or understand how module interactions shape agent behavior. We introduce AgentSpec, a modular specification framework that represents embodied agents as typed compositions of reusable policy components with standardized interfaces. AgentSpec standardizes the interfaces among perception, memory, reasoning, reflection, action, and optional learning, enabling components to be swapped and recombined under controlled conditions. We instantiate this framework across DeliveryBench, ALFRED, MiniGrid, and RoboTHOR, and analyze reasoning, memory, reflection, and reinforcement-learning modules across model backbones. Our results show that agent performance is governed by scaffold compatibility and interaction effects rather than isolated module strength. In particular, structured multi-granularity memory improves long-horizon state tracking, reasoning and memory interact non-uniformly across environments, reflection trades off correction and cost, and RL-trained policies compose best when optimized with deployment-time scaffold structure. AgentSpec provides a controlled foundation for studying, comparing, and designing composable LLM agents. Our code, baselines and interactive playground are publicly available at https://agentspec-embodied.github.io.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
