# Memory Without Curation: Learning Multi-Stream Latent Memory for Robot Policies

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.14406v1
- Published: 2026-10-09
- Updated: 2026-10-09
- Authors: Yilin Wu, Rutav Shah, Shuaiyi Huang, Sumedh A. Sontakke, Homanga Bharadhwaj, Andrea Bajcsy, Max Simchowitz, Guanya Shi
- Tags: long-term
- Categories: cs.RO, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.14406v1

## One-Sentence Summary
It is widely appreciated that robotic policies require long-term memory to perform complex tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：It is widely appreciated that robotic policies require long-term memory to perform complex tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, directly conditioning policies on all past observations leaves policy learning susceptible to learning spurious shortcuts, and introduces large latency at policy deployment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.RO, cs.AI, cs.LG

## Abstract Snapshot
It is widely appreciated that robotic policies require long-term memory to perform complex tasks. However, directly conditioning policies on all past observations leaves policy learning susceptible to learning spurious shortcuts, and introduces large latency at policy deployment. As such, today's memory-augmented policies curate what to remember, either by retaining only recent frames, selected keyframes, or textual summaries, or by learning latent representations of the visual stream alone. In this work, we propose an alternative approach IMPRINT, a policy-agnostic latent memory framework that augments vision-language-action (VLA) models with multi-stream memory without explicitly constraining what the policy should remember. IMPRINT compresses different streams into a latent memory that is updated incrementally at inference, enabling low latency. To avoid shortcut learning, IMPRINT adopts a two-stage training procedure, first supervising memory to reconstruct multiple streams (observations, actions, proprioception) of past information, as well as estimate current task progress, followed by end-to-end finetuning, jointly with the policy, on action prediction. Across both simulation and real-world tasks demanding memory, IMPRINT improves average success over the base VLA by at least 26%, outperforming popular alternatives, and maintaining lowest inference latency among memory-augmented VLAs. Through careful ablations, we demonstrate the utility of incorporating diverse information streams into robotic memory, validating the advantages of foregoing history curation. Project website: https://yilin-wu98.github.io/imprint_website/.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
