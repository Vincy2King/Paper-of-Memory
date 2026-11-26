# Procedure Inference as Memory: Learning Recruiter Decision Procedures from OKF-Structured Episodes in Multi-Session Hiring Assistants

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.34576v1
- Published: 2026-11-25
- Updated: 2026-11-25
- Authors: Praveen Kumar Bodigutla, Yizhi Zhang, Sai Vivek Kanaparthy, Arup De
- Tags: context, conversation, episodic, retrieval
- Categories: cs.AI, cs.HC, cs.IR
- URL: http://arxiv.org/abs/2611.34576v1

## One-Sentence Summary
Multi-session hiring assistants must infer evolving recruiter preferences and decision patterns across projects and time.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-session hiring assistants must infer evolving recruiter preferences and decision patterns across projects and time.

进一步看，论文的核心做法或实验重点可以概括为：We introduce Open Knowledge Format (OKF)-indexed episodic memory to organize interactions and retrieve related events through their lineage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.HC, cs.IR

## Abstract Snapshot
Multi-session hiring assistants must infer evolving recruiter preferences and decision patterns across projects and time. We introduce Open Knowledge Format (OKF)-indexed episodic memory to organize interactions and retrieve related events through their lineage. We also introduce Procedure Memory, which learns reusable decision procedures from these episodes through prompted reflection or reinforcement learning. We compare these approaches with no memory, full-history context, and conversation search, and evaluate Jev-class models for index navigation and GPT-5.6 Luna as a lower-cost alternative to GPT-5.4. In our evaluation, OKF-indexed retrieval achieves low-priority preference F1 scores of 0.93-0.95 at medium and high preference overlap between hiring projects. It significantly outperforms full-history context and conversation search in both settings, and no memory at high overlap, while using 69% fewer context tokens than full history. Procedure Memory reduces conversational turns by up to 39% relative to no memory. Qualitative and long-horizon evaluations provide evidence of temporal reasoning, with RL-learned procedures achieving 60% on both correct abstention and exact-field identification. Jev-class models improve conversational efficiency but more frequently miss temporally relevant evidence, highlighting the importance of evidence selection. On PersonaMem-v2, Procedure Memory with OKF retrieval achieves 50.2% accuracy versus 48.6% for full-history context and 29.0% for no memory, using 90.5% fewer reader input tokens than full history. GPT-5.6 Luna performs comparably to GPT-5.4 at lower cost. These findings highlight the value of structured episodic memory and learned decision procedures for efficient personalization and temporal reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
