# ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.01058v1
- Published: 2026-09-01
- Updated: 2026-09-01
- Authors: Fanrui Zhang, Ruixue Ding, Qiang Zhang, Xi Chen, Boli Chen, Shihang Wang, Qiuchen Wang, Hongmin Zhan, Jinxin Bian, Li xingchao, Peijin Zheng, Hao cheng, Pengjun Xie, Kaipeng Zhang, Jiawei Liu, Zheng-Jun Zha
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.01058v1

## One-Sentence Summary
Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics.

进一步看，论文的核心做法或实验重点可以概括为：Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout contrast that obscures fine-grained optimization...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout contrast that obscures fine-grained optimization signals for group-based policy learning. To address these challenges, we propose ARISE-RL, a novel full-cycle self-evolution framework that couples a task/rubric Generator and a reasoning Solver through rubric-mediated co-evolution. The Generator grounds tool-related rubric criteria in real tool observations and is rewarded for producing valid, intermediate-difficulty tasks aligned with the Solver's evolving capability boundary. The Solver, in turn, learns from fine-grained rubric satisfaction signals through multi-step reasoning and tool use. We further introduce Reward-Gated Self-Evolution Distillation (RG-SED), which selectively distills a memory-augmented variant of the same policy back into itself only when the memory yields empirical reward improvement, thereby reducing distribution mismatch and avoiding blind imitation of noisy guidance. Finally, to support rigorous evaluation, we present ECR-Bench, an expert-calibrated rubric benchmark suite covering single-tool deep research and multi-tool travel planning. Extensive experiments demonstrate that ARISE-RL consistently achieves robust and stable overall state-of-the-art performance across all evaluated benchmarks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
