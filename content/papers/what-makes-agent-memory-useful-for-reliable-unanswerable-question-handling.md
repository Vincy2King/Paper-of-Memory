# What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.27924v1
- Published: 2026-08-28
- Updated: 2026-08-28
- Authors: Chuanyuan Tan, Junjie Yu, Yuxin Wang, Yining Zheng, Xipeng Qiu, Wenliang Chen
- Tags: agent
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.27924v1

## One-Sentence Summary
Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents.

进一步看，论文的核心做法或实验重点可以概括为：Although memory is widely used in agent systems, its role in reliable UAQ handling remains unclear.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents. Although memory is widely used in agent systems, its role in reliable UAQ handling remains unclear. We present a systematic study of agent memory for UAQ handling under a unified agentic RAG framework, evaluating four representative memory methods across three UAQ-related datasets and two base models. We find that memory can improve UAQ performance in some settings, but such gains are selective rather than universal and remain fragile under dataset shift. Interestingly, cross-model memory reuse is often more feasible than cross-dataset transfer, suggesting that shifts in answerability patterns pose a greater challenge to memory reuse than changes in the base model itself. We further find that UAQ gains are more strongly preserved through decision guidance than through trajectory shaping, and that memory effectiveness depends strongly on representation. In particular, procedural and rule-based memories often provide the most reliable support for UAQ handling, while memory composition is most effective when procedural guidance is combined with complementary behavioral signals. Overall, our findings suggest that reliable UAQ memory depends less on storing larger amounts of experience and more on preserving transferable behavioral guidance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
