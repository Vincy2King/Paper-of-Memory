# RGMem: Renormalization Group-inspired Memory Evolution for Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2510.16392v3
- Published: 2025-10-18
- Updated: 2026-06-02
- Authors: Ao Tian, Yunfeng Lu, Xinxin Fan, Changhao Wang, Lanzhi Zhou, Yeyao Zhang, Yanfang Liu
- Tags: agent, benchmark, context, conversation, episodic, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2510.16392v3

## One-Sentence Summary
Personalized and continuous interactions are critical for LLM-based conversational agents, yet finite context windows and static parametric memory hinder the modeling of long-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized and continuous interactions are critical for LLM-based conversational agents, yet finite context windows and static parametric memory hinder the modeling of long-term, cross-session user states.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches, including retrieval-augmented generation and explicit memory systems, primarily operate at the fact level, making it difficult to distill stable preferences and deep user traits from evolving and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, episodic, long-term
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Personalized and continuous interactions are critical for LLM-based conversational agents, yet finite context windows and static parametric memory hinder the modeling of long-term, cross-session user states. Existing approaches, including retrieval-augmented generation and explicit memory systems, primarily operate at the fact level, making it difficult to distill stable preferences and deep user traits from evolving and potentially conflicting dialogues.To address this challenge, we propose RGMem, a self-evolving memory framework inspired by the renormalization group (RG) perspective on multi-scale organization and emergence. RGMem models long-term conversational memory as a multi-scale evolutionary process: episodic interactions are transformed into semantic facts and user insights, which are then progressively integrated through hierarchical coarse-graining, thresholded updates, and rescaling into a dynamically evolving user profile.By explicitly separating fast-changing evidence from slow-varying traits and enabling non-linear, phase-transition-like dynamics, RGMem enables robust personalization beyond flat retrieval or static summarization. Extensive experiments on the LOCOMO and PersonaMem benchmarks demonstrate that RGMem consistently outperforms SOTA memory systems, achieving stronger cross-session continuity and improved adaptation to evolving user preferences. Code is available at https://github.com/fenhg297/RGMem

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
