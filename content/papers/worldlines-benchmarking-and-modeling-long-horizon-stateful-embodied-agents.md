# WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.18847v1
- Published: 2026-06-17
- Updated: 2026-06-17
- Authors: Yehang Zhang, Jianchong Su, Haojian Huang, Yifan Chang, Tianhao Zhou, Xinli Xu, Yingjie Xu, Yinchuan Li, Zexi Li, Ying-Cong Chen
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.18847v1

## One-Sentence Summary
To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while embodied benchmarks often focus on short-horizon task execution without testing long-term memory use in...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while embodied benchmarks often focus on short-horizon task execution without testing long-term memory use in dynamic environments. We introduce WorldLines, a project-driven benchmark for long-horizon embodied household assistance. It constructs temporally extended household traces with dialogues, actions, execution feedback, object and device state changes, and converts them into evidence-linked samples for Memory QA and Embodied Task Planning. We further propose ObsMem, an observer-grounded memory framework that maintains visibility-aware memories and action-native state trails for state-aware decisions. Experiments reveal persistent challenges in partial observability, overwritten world states, and translating long-term memory into embodied plans, while ObsMem offers a stronger reference architecture for this setting.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
