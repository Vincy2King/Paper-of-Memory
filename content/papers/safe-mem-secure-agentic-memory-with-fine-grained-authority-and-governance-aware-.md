# SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.22959v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Haoming Li, Dingyi Kang, Xu Hu, Jinxin Yang, Zhu Xu, Chenru Wang, Yi Ge, Miao Yin, Guanpeng Li, Feng Chen, Bingzhe Li
- Tags: agent, long-term, retrieval
- Categories: cs.CR, cs.CL
- URL: http://arxiv.org/abs/2610.22959v1

## One-Sentence Summary
Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.CR, cs.CL

## Abstract Snapshot
Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at https://github.com/LVenum/SAFE-Mem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
