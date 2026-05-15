# GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.14498v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Shiyu Chang, Yaar Harari, Evgeniy Gabrilovich
- Tags: agent, benchmark, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.14498v1

## One-Sentence Summary
Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running...

进一步看，论文的核心做法或实验重点可以概括为：However, both existing memory systems and benchmarks are built around the dyadic, single-user setup, even though real deployments routinely span groups and channels with multiple users interacting with the agent and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations. However, both existing memory systems and benchmarks are built around the dyadic, single-user setup, even though real deployments routinely span groups and channels with multiple users interacting with the agent and with each other. This mismatch leaves three properties of group memory unmeasured: (i) group dynamics that go beyond concatenated one-on-one chats, (ii) speaker-grounded belief tracking, where the per-user memory modeling is needed, and (iii) audience-adapted language, where Theory-of-Mind shifts produce role-specific vocabulary. We introduce GroupMemBench, a benchmark that exposes all three. A graph-grounded synthesis pipeline produces multi-party conversations with controllable reply structure and conditions each message on per-user personas and target audiences. An adversarial query pipeline then binds every question to a specific asker across six categories, spanning multi-hop reasoning, knowledge update, term ambiguity, user-implicit reasoning, temporal reasoning, and abstention, and iteratively searches challenging, realistic queries that reflect comprehensive memory capability. Benchmarking leading memory systems exposes a sharp collapse: the strongest one reaches only 46.0% average accuracy, with knowledge update at 27.1% and term ambiguity at 37.7%, while a simple BM25 baseline matches or exceeds most agent memory systems. This indicates current memory ingestion erases the structural and lexical features group memory depends on, leaving multi-user memory far from solved.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
