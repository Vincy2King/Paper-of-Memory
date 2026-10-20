# MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25127v1
- Published: 2026-10-18
- Updated: 2026-10-18
- Authors: Jiajun Tan, Fei Sun, Xinyu Ma, Shixuan Zhang, Du Su, Qi Cao, Daiting Shi, Huawei Shen, Xueqi Cheng
- Tags: agent, benchmark, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.25127v1

## One-Sentence Summary
Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, its use may reduce response diversity, thereby narrowing the range of information available to users.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions. However, its use may reduce response diversity, thereby narrowing the range of information available to users. Existing evaluations rely largely on synthetic interactions and cover few memory systems, leaving the effects of memory on response diversity insufficiently evaluated in real-world scenarios. We introduce MemBubble, a benchmark of 1000 instances built on preferences extracted from real user-assistant conversations. To measure the extent to which memory concentrates response distributions, we construct test queries in scenarios distinct from user preferences while preserving topical relevance through shared preference categories. Across multiple LLMs and memory mechanisms, entropy decreases by 34.7% on average compared with directly providing the full interaction history, highlighting the important role of memory processing in diversity loss. We also explore simple user-side interventions and changes in information availability but find that these do not effectively close the diversity gap. Our findings highlight the need to consider preserving diversity and user access to information alongside improvements in personalization when designing and using agent memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
