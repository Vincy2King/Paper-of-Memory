# VMSA: Video Memory Skill Agent for Long Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.27381v1
- Published: 2026-11-20
- Updated: 2026-11-20
- Authors: Changin Choi, Jungwon Park, Jungmin Ko, Jimyeong Kim, Wonjong Rhee
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2611.27381v1

## One-Sentence Summary
Long-video question answering requires retrieving and integrating relevant evidence from videos spanning hours or even days.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-video question answering requires retrieving and integrating relevant evidence from videos spanning hours or even days.

进一步看，论文的核心做法或实验重点可以概括为：Recent agentic approaches organize video information into external memories and iteratively retrieve evidence to answer questions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Long-video question answering requires retrieving and integrating relevant evidence from videos spanning hours or even days. Recent agentic approaches organize video information into external memories and iteratively retrieve evidence to answer questions. However, effective retrieval and reasoning remain challenging, as agents must determine what information to search for, which memory sources to access, and how to connect evidence across distant temporal intervals. To address these challenges, we propose Video Memory Skill Agent (VMSA), a framework that jointly designs structured video memories and memory skills for long-video understanding. VMSA constructs three complementary memory components. Segment Caption Memory and Entity Event Memory serve as searchable evidence sources, while Entity-Aware Episode Memory provides broad yet detailed video context to guide evidence retrieval and reasoning. To further support effective memory utilization, VMSA induces memory skills from successful agent trajectories, incrementally refining or extending a compact skill library to guide iterative evidence retrieval, reasoning, and verification. Across seven long-video question-answering benchmarks, VMSA achieves the highest accuracy on all three week-long egocentric benchmarks, outperforming the strongest baseline by up to 9.4% on Ego-R1 Bench, and the best or competitive performance on four additional benchmarks. Ablation studies further demonstrate the contributions of all three memory components and memory skills, with memory skills also improving temporal evidence localization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
