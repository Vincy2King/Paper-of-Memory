# Evaluating the Hidden Costs of Personalization in Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.28833v1
- Published: 2026-08-28
- Updated: 2026-08-28
- Authors: Yumeng Wang, Yuchen Wu, Cheng Qian, Zhiyuan Fan, Hyeonjeong Ha, Shujin Wu, Jiayu Liu, Heng Ji, Ge Wang
- Tags: context, conversation
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.28833v1

## One-Sentence Summary
While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative responses toward optimizing for user...

进一步看，论文的核心做法或实验重点可以概括为：Specifically, we identify three emerging risks: (1) irrelevant personalization, where models reference personal information in unnecessary contexts; (2) preference narrowing, where models reinforce informational echo...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative responses toward optimizing for user satisfaction when conditioned on personal context such as conversation history, inferred preferences, and user profiles. Specifically, we identify three emerging risks: (1) irrelevant personalization, where models reference personal information in unnecessary contexts; (2) preference narrowing, where models reinforce informational echo chambers; and (3) sycophantic bias, where models agree excessively with user opinions. As a result, models may reference personal information in contexts where it is unnecessary, inadvertently collapse response diversity, or agree excessively with user opinions. Despite the growing use of personalization in AI assistants, there has been limited systematic evaluation of its potential side effects. To bridge this gap, we propose PRISK, a dynamic evaluation framework with automated data generation and tailored metrics that uncovers systematic limitations in current LLM personalization and how personalized information shapes its responses. Our empirical analysis across 13 LLMs demonstrates the presence of user profiles and retrieved memories consistently exacerbates biases, resulting in an average drop of 45.9% in irrelevant personalization, 41.7% in preference narrowing and 61.7% in sycophantic bias.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
