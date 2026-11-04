# The Right Source Is Not Enough: Understanding History Interference in Speech-LLM Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.05124v1
- Published: 2026-11-03
- Updated: 2026-11-03
- Authors: HongJin Song, Weiqiao Shan, Runwu Shi, Yifei Wu, Yujin Wang, Jiale Luo, Jiasheng Kuang, Xinyu Yang, Zhaoqi Cui, Chuizheng Kong, Ziyu Wu, Guowu Tan, Qiuyu Fang, Chunxiang Jin
- Tags: context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2611.05124v1

## One-Sentence Summary
Speech large language models retain audio history to support multi-turn conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Speech large language models retain audio history to support multi-turn conversations.

进一步看，论文的核心做法或实验重点可以概括为：Yet remembering an event does not ensure that its information is used only when relevant.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Speech large language models retain audio history to support multi-turn conversations. Yet remembering an event does not ensure that its information is used only when relevant. We investigate why irrelevant historical audio changes answers even when the queried event remains represented. Controlled experiments on MOSS-Audio and MiMo-Audio show that historical values direct errors toward specific competing answers, beyond a generic effect of context length. Causal interventions distinguish two paths. In open-ended question answering, most history-value errors disappear when subsequent computation cannot directly access the irrelevant source. In multiple-choice answering, many errors persist: early historical influence is carried by question-candidate states even after direct source access is blocked. Low-dimensional interventions further separate source-role information from answer-value information. Their effects peak at different depths, and changing the source-role signal does not eliminate the causal influence of competing values. On naturally occurring errors, strengthening the queried role and counteracting the historical value each improve answers; their joint intervention gives the greatest recovery. These findings support a failure of downstream evidence use beyond source identification alone: source-role information can influence a decision without exclusively controlling which historical values affect it. Reliable conversational memory therefore requires not only retention and retrieval, but also control over how retained information enters answer computation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
