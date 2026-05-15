# When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.14504v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Zilin Zhu, Longteng Guo, Yanghong Mei, Bowen Pang, Zongxun Zhang, Xingjian He, Ruyi Ji, Jing Liu
- Tags: agent, benchmark, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.14504v1

## One-Sentence Summary
Long-horizon household tasks demand robust high-level planning and sustained reasoning capabilities, which are largely overlooked by existing embodied AI benchmarks that...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon household tasks demand robust high-level planning and sustained reasoning capabilities, which are largely overlooked by existing embodied AI benchmarks that emphasize short-horizon navigation or...

进一步看，论文的核心做法或实验重点可以概括为：We introduce LongAct, a benchmark designed to evaluate planning-level autonomy in long-horizon household tasks specified through free-form instructions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon household tasks demand robust high-level planning and sustained reasoning capabilities, which are largely overlooked by existing embodied AI benchmarks that emphasize short-horizon navigation or manipulation and rely on fixed task categories. We introduce LongAct, a benchmark designed to evaluate planning-level autonomy in long-horizon household tasks specified through free-form instructions. By abstracting away embodiment-specific low-level control, LongAct isolates high-level cognitive capabilities such as instruction understanding, dependency management, memory maintenance, and adaptive planning. We further propose HoloMind, a VLM-driven agent with a DAG-based long-horizon hierarchical planner, a Multimodal Spatial Memory for persistent world modeling, an Episodic Memory for experience reuse, and a global Critic for reflective supervision. Experiments with GPT-5 and Qwen3-VL models show that HoloMind substantially improves long-horizon performance while reducing reliance on model scale. Even top models achieve only 59% goal completion and 16% full-task success, underscoring the difficulty of LongAct and the need for stronger long-horizon planning in embodied agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
