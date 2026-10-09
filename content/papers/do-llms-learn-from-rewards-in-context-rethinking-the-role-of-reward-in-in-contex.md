# Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11152v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, Junmo Kim
- Tags: agent, benchmark, context
- Categories: cs.LG, cs.CL
- URL: http://arxiv.org/abs/2610.11152v1

## One-Sentence Summary
LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters.

进一步看，论文的核心做法或实验重点可以概括为：This process is often described as in-context reinforcement learning (ICRL).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, cs.CL

## Abstract Snapshot
LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters. This process is often described as in-context reinforcement learning (ICRL). Whether in-context learning (ICL) can actually play the role of RL, however, has not been tested. We study this question in its simplest form, direct ICRL, where the model conditions directly on raw trajectory-reward pairs, and ask whether the reward acts as a learning signal. Through controlled experiments on four benchmarks across six models, we find that the reward is read, but its effect is small: flipping, randomizing, or removing the reward leaves the improvement curve almost unchanged, and this holds even under meta-prompts that explicitly instruct the model to explore, exploit, or reason over rewards. Trajectories drive improvement, but not through their semantic content: shuffled or corrupted trajectories work as well as real ones. These patterns closely mirror those known in ICL, suggesting that direct ICRL is better understood as a special case of ICL than as inference-time RL. This reframing has implications for agent memory design: ICL factors such as input distribution and demonstrations may matter more than RL elements such as reward shaping and exploration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
