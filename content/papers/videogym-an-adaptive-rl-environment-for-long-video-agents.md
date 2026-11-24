# VideoGym: An Adaptive RL Environment for Long-Video Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.28102v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Jing Wang, Yi Ke Yun, Yifeng Yao, Huishuai Zhang, Dongyan Zhao, Tao Wang
- Tags: agent, benchmark, retrieval
- Categories: cs.CV, cs.AI, cs.MM
- URL: http://arxiv.org/abs/2611.28102v1

## One-Sentence Summary
Reinforcement learning (RL) trains video agents to locate sparse evidence for long-video question answering through structured memory retrieval and temporal re-observation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reinforcement learning (RL) trains video agents to locate sparse evidence for long-video question answering through structured memory retrieval and temporal re-observation.

进一步看，论文的核心做法或实验重点可以概括为：This training, however, faces a long-tail modality distribution in the data.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory augmented, memory retrieval, memory-augmented
- 来源分类信息：cs.CV, cs.AI, cs.MM

## Abstract Snapshot
Reinforcement learning (RL) trains video agents to locate sparse evidence for long-video question answering through structured memory retrieval and temporal re-observation. This training, however, faces a long-tail modality distribution in the data. In our source pool, text-heavy questions account for 58% of samples, compared with 15% graph-heavy, 17% visual-heavy, and 10% time-range questions. Fixed-distribution RL therefore allocates fewer rollouts to underperforming question types. Reweighting these types could increase their sampling frequency but repeatedly reuses the same finite banks of original questions. To solve this problem, we introduce VideoGym, a curriculum-based RL environment that jointly constructs video-grounded training tasks and allocates rollouts among them. Within the environment, a memory-augmented VideoAgent is trained to coordinate retrieval from text, graph, and visual memories with temporal re-observation. Across episodes, VideoGym adapts VideoAgent's training distribution online: it casts per-period sample selection as an adversarial bandit over (modality, mode) arms and applies the EXP3 update to shift sampling toward arms with low answer accuracy. To supply the augmented-mode arms, a TaskGenerator-Verifier pipeline produces harder variants of existing questions that remain answerable within the same video. Across five long-video benchmarks, VideoGym lifts RL accuracy from 60.4% to 64.8% on average and by up to 10.5 pp on underrepresented graph-heavy questions with 3.3x sample efficiency. Together, these results show that task expansion and adaptive allocation can improve video agent learning from limited, imbalanced training data.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
