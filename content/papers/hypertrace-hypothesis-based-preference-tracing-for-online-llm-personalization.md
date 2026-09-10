# HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.09835v1
- Published: 2026-09-09
- Updated: 2026-09-09
- Authors: Jianzhi Shen, Keyu Mao, Minghao Shao, Chuanyang Jin, Yusong Wang, Ailiang Lin, Kotaro Funakoshi, Manabu Okumura, Tianmin Shu, Muhammad Shafique
- Tags: long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.09835v1

## One-Sentence Summary
Personalized language models aim to adapt responses to individual users, whose preferences are often latent and revealed gradually through interaction.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized language models aim to adapt responses to individual users, whose preferences are often latent and revealed gradually through interaction.

进一步看，论文的核心做法或实验重点可以概括为：Existing training-free methods rely on stored histories or retrieved memories, but they often struggle to reconcile long- term preferences with short-term topic-specific needs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Personalized language models aim to adapt responses to individual users, whose preferences are often latent and revealed gradually through interaction. Existing training-free methods rely on stored histories or retrieved memories, but they often struggle to reconcile long- term preferences with short-term topic-specific needs. To address this issue, we propose HyperTrace, a training-free framework that formulates online personalization as latent preference tracing. HyperTrace maintains interpretable natural-language hypotheses over short-term intent and long-term preferences, and updates them through an SMC-style reweight process using an LLM-based surrogate choice model. By updating these hypotheses across turns and sessions, HyperTrace enables personalization without parameter updates. Experiments on PRISM and PersonaMem-v2 show that HyperTrace improves response alignment, preference prediction, and profile consistency over strong online baselines, demonstrating the effectiveness of tracing latent user preferences for robust personalization. Code and scripts are available in the repository: https://github.com/jiseshen/HyperTrace.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
