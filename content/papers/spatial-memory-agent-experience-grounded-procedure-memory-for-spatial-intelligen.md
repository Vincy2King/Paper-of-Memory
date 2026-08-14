# Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.12743v1
- Published: 2026-08-13
- Updated: 2026-08-13
- Authors: Haokai Zhang, Yuhang Ding, Yunshu Zhou, Xinze Du, Shengtao Zhang, Zhiyue Zhao, Yuling Xi, Hao Chen
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.12743v1

## One-Sentence Summary
Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants.

进一步看，论文的核心做法或实验重点可以概括为：To improve the spatial reasoning ability of VLM agents, existing work has mainly followed two lines.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants. To improve the spatial reasoning ability of VLM agents, existing work has mainly followed two lines. One line uses post-training methods, such as supervised fine-tuning and reinforcement learning. Another line adopts an agentic paradigm in which the model calls external spatial tools, such as depth estimation and 3D reconstruction tools, to gather intermediate spatial evidence. We study a complementary and underexplored route: Can a frozen VLM agent improve its spatial reasoning through \textbf{parameter-update-free self-evolution}, without depending on external expert spatial tools at inference time? We present \textbf{Spatial Memory Agent (SMA)}, an \textbf{experience-grounded runtime framework} that converts verified spatial experience into reusable transferable lessons. In a verifiable spatial environment, SMA queries the frozen VLM, obtains a predicted answer and reward, and uses \textbf{verifier-guided reflection} to distill compact transferable lessons from spatial experience. SMA further assigns each lesson a \textbf{Transfer Reliability Score (TRS)}, which is initialized uniformly and calibrated from later retrieval outcomes as visit evidence of future transfer reliability. During \textbf{read-only deployment}, SMA retrieves lessons by semantic filter and similarity-TRS combined ranking, allowing the retrieved memory to guide frozen model inference. Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free path for spatial self-evolution across the evaluated frozen model scales and environments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
