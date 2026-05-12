# Continual Harness: Online Adaptation for Self-Improving Foundation Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09998v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Seth Karten, Joel Zhang, Tersoo Upaa, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli
- Tags: agent, context
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2605.09998v1

## One-Sentence Summary
Coding harnesses such as Claude Code and OpenHands wrap foundation models with tools, memory, and planning, but no equivalent exists for embodied agents' long-horizon partial-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Coding harnesses such as Claude Code and OpenHands wrap foundation models with tools, memory, and planning, but no equivalent exists for embodied agents' long-horizon partial-observability decision-making.

进一步看，论文的核心做法或实验重点可以概括为：We first report our Gemini Plays Pokemon (GPP) experiments.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Coding harnesses such as Claude Code and OpenHands wrap foundation models with tools, memory, and planning, but no equivalent exists for embodied agents' long-horizon partial-observability decision-making. We first report our Gemini Plays Pokemon (GPP) experiments. With iterative human-in-the-loop harness refinement, GPP became the first AI system to complete Pokemon Blue, Yellow Legacy on hard mode, and Crystal without a lost battle. In the hardest stages, the agent itself began iterating on its strategy through long-context memory, surfacing emergent self-improvement signals alongside human-in-the-loop refinement. Continual Harness removes the human fully from this loop: a reset-free self-improving harness for embodied agents that formalizes and automates what we observed. Starting from only a minimal environment interface, the agent alternates between acting and refining its own prompt, sub-agents, skills, and memory, drawing on any past trajectory data. Prompt-optimization methods require episode resets; Continual Harness adapts online within a single run. On Pokemon Red and Emerald across frontier models, Continual Harness starting from scratch substantially reduces button-press cost relative to the minimalist baseline and recovers a majority of the gap to a hand-engineered expert harness, with capability-dependent gains, despite starting from the same raw interface with no curated knowledge, no hand-crafted tools, and no domain scaffolding. We then close the loop with the model itself: an online process-reward co-learning loop, in which an open-source agent's rollouts through the refining harness are relabeled by a frontier teacher and used to update the model, drives sustained in-game milestone progress on Pokemon Red without resetting the environment between training iterations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
