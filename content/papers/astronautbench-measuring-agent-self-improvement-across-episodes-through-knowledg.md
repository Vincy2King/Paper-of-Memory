# AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.26910v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Congyuan Yu, Runping Tian
- Tags: agent, benchmark, episodic
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2611.26910v1

## One-Sentence Summary
LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights.

进一步看，论文的核心做法或实验重点可以概括为：Self-improvement in an embodied world cannot be read from one measure.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights. Self-improvement in an embodied world cannot be read from one measure. Existing benchmarks measure task progress, world-knowledge question answering (QA), and episodic memory, but a correct answer does not show that the agent ever observed the evidence for it, and progress does not show what the agent learned. We introduce AstronautBench, which measures one agent's self-improvement through three views on the same run: what it knows, whether its own evidence supports that knowledge, and how far it gets in the world. It is built on the game Outer Wilds, where each episode is a 22-minute loop after which the world resets, only the agent's knowledge carries over, and progress is gated by knowledge. After every episode, we measure the places reached and ship-log rumor facts revealed, the correctness of answers to 164 questions about the world, and whether each answer is supported by the frames and position the agent cites from its own recorded play. Two LLM judges from different model families check every answer. In eight-episode baselines with GPT-6.1 Sol and Gemini 4 Argon planners, which act through a learned controller or their own gamepad inputs, the three views do not move together, so any one of them alone gives an incomplete picture of whether the agent is improving. The GPT-6.1 Sol agent's correct answers grow from 14.6% to 26.8% of all questions, but at episode 8 only 59 to 68% of them are supported by its cited evidence. It reveals no new rumor facts after episode 3, while the places it reaches and its memory keep growing. More than half of the answers that become correct after episode 3 cite only evidence from earlier episodes.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
