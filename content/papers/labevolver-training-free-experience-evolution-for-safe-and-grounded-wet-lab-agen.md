# LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.27690v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Jingya Wang, Yuyang Gao, Liuzhenghao Lv, Yonghong Tian, Yuyang Liu
- Tags: agent, episodic
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2607.27690v1

## One-Sentence Summary
We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience.

进一步看，论文的核心做法或实验重点可以概括为：LabEvolver couples a state-grounded inner trial loop for adaptive perception, online planning, and safety validation with an outer evolution loop that distills completed trajectories into reusable skill, strategy, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience. LabEvolver couples a state-grounded inner trial loop for adaptive perception, online planning, and safety validation with an outer evolution loop that distills completed trajectories into reusable skill, strategy, and safety experience. On robotic solution-preparation tasks, LabEvolver demonstrates real-world feasibility, reducing pH-regulation completion time and safety-gate intercepts by 48.2% and 60.0%, respectively. On ALFWorld, it further improves cumulative success rate within 20 steps from 76.2% with ReAct to 91.4% over 500 continual tasks, showing generality beyond wet-lab settings. These results support learn-by-doing experience evolution as a feasible path toward closed-loop automated scientific discovery. The project page is available at https://github.com/AndyGao6186/LabEvolver.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
