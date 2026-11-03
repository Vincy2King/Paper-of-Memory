# SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.01695v1
- Published: 2026-11-01
- Updated: 2026-11-01
- Authors: Hangming Zhang, Yao Zhao, Haotian Kuang, C. L. Philip Chen, Tong Zhang, Tengyue Ma
- Tags: agent, context, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.01695v1

## One-Sentence Summary
B2B outbound sales involves high transaction values and relationship-based trust, so closing a deal typically requires multiple rounds of outreach building on prior context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：B2B outbound sales involves high transaction values and relationship-based trust, so closing a deal typically requires multiple rounds of outreach building on prior context.

进一步看，论文的核心做法或实验重点可以概括为：Existing LLM-based sales agents operate within single sessions and cannot carry forward context or refine strategies from experience.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
B2B outbound sales involves high transaction values and relationship-based trust, so closing a deal typically requires multiple rounds of outreach building on prior context. Existing LLM-based sales agents operate within single sessions and cannot carry forward context or refine strategies from experience. Methods that do learn from experience store lessons as unstructured text and treat all outcomes as equally informative, with no mechanism to distinguish a flawed strategy from an external factor. We propose SPAR, a self-evolving framework that models selling strategies as testable hypotheses and refines them without parameter updates. A double-loop architecture lets an inner loop adapt to individual merchants through episodic memory while an outer loop evolves a shared strategy playbook through causal attribution and hypothesis-driven evolution. In a live A/B test on the 1688 platform with over 200,000 merchants, SPAR achieves +15.8% conversion lift and +35.8% high-intent merchant growth. Human evaluation by domain experts rates SPAR at 4.62 out of 5 on overall sales quality, the highest among all methods.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
