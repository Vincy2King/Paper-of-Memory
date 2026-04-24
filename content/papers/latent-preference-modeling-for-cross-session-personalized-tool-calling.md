# Latent Preference Modeling for Cross-Session Personalized Tool Calling

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.17886v1
- Published: 2026-04-20
- Updated: 2026-04-20
- Authors: Yejin Yoon, Minseo Kim, Taeuk Kim
- Tags: agent, benchmark
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.17886v1

## One-Sentence Summary
Users often omit essential details in their requests to LLM-based agents, resulting in under-specified inputs for tool use.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Users often omit essential details in their requests to LLM-based agents, resulting in under-specified inputs for tool use.

进一步看，论文的核心做法或实验重点可以概括为：This poses a fundamental challenge for tool-augmented agents, as API execution typically requires complete arguments, highlighting the need for personalized tool calling.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Users often omit essential details in their requests to LLM-based agents, resulting in under-specified inputs for tool use. This poses a fundamental challenge for tool-augmented agents, as API execution typically requires complete arguments, highlighting the need for personalized tool calling. To study this problem, we introduce MPT, a benchmark comprising 265 multi-session dialogues that cover three challenges: Preference Recall, Preference Induction, and Preference Transfer. We also propose PRefine, a test-time memory-augmented method that represents user preferences as evolving hypotheses. Through a generate--verify--refine loop, it extracts reusable constraints from history and improves tool-calling accuracy while using only 1.24% of the tokens required by full-history prompting. These results indicate that robust personalization in agentic systems depends on memory that captures the reasons behind user choices, not just the choices themselves.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
