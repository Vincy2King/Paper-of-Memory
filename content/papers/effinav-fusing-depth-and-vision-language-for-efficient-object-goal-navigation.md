# EffiNav: Fusing Depth and Vision-Language for Efficient Object Goal Navigation

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.18634v1
- Published: 2026-06-17
- Updated: 2026-06-17
- Authors: Zecheng Yin, Benedict Jun Ma
- Tags: agent, benchmark
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2606.18634v1

## One-Sentence Summary
To locate a target object while exploring the unknown environment is a fundamental capability for autonomous agents, with applications ranging from search-and-rescue to field...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：To locate a target object while exploring the unknown environment is a fundamental capability for autonomous agents, with applications ranging from search-and-rescue to field robots.

进一步看，论文的核心做法或实验重点可以概括为：A simplified version of such task is Object Goal Navigation (ObjNav).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
To locate a target object while exploring the unknown environment is a fundamental capability for autonomous agents, with applications ranging from search-and-rescue to field robots. A simplified version of such task is Object Goal Navigation (ObjNav). In ObjNav, successful arrival at the target object provides a basic measure of performance; however, the efficiency of the navigation trajectory is equally important, as it indicates how intelligently the agent explores and how much time remains for subsequent tasks. In unknown environments, the key to efficient navigation lies in deciding where to explore next. While many prior works aim to address this core challenge and achieved promising performance in certain settings, recent training-based models and non-training frameworks still suffer from generalization and efficiency issues respectively, which in the worst cases can lead to excessive exploration of already-visited areas or redundant back-and-forth motion. We evaluate EffiNav on two widely used simulation benchmarks Habitat Matterport 3D (HM3D) and Open-Vocabulary Object goal Navigation (OVON), and further validate its effectiveness on physical robots in real-world settings. We conduct failure analysis on massive simulation episodes. With minimal modification, we also extend EffiNav to a memory-augmented ObjNav task on the GOAT-BENCH dataset, demonstrating its adaptability beyond standard ObjNav settings. Across two standard metrics--Success Rate (SR) and Success weighted by Path Length (SPL), EffiNav matches or outperforms recent baselines, reflecting its efficiency, robustness, and practical applicability. Recognizing the different emphases of the two datasets, the performances reveals this framework is more balanced and generalizable for efficient ObjNav.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
