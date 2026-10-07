# Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07403v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Ritvij Sharma, Russell Dlugosz, Ryan Zhou, Maheep Chaudhary
- Tags: context, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.07403v1

## One-Sentence Summary
Long-term memory allows Large Language Models (LLMs) to maintain personalized context across interactions, but retrieved user history can induce memory-induced sycophancy,...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory allows Large Language Models (LLMs) to maintain personalized context across interactions, but retrieved user history can induce memory-induced sycophancy, causing models to favor stored user beliefs...

进一步看，论文的核心做法或实验重点可以概括为：Existing defenses primarily operate on retrieved context and are rarely evaluated jointly with internal behavioral bias.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory allows Large Language Models (LLMs) to maintain personalized context across interactions, but retrieved user history can induce memory-induced sycophancy, causing models to favor stored user beliefs over objective evidence. Existing defenses primarily operate on retrieved context and are rarely evaluated jointly with internal behavioral bias. We introduce a $2 \times 2$ defense-in-depth framework separating internal activation steering from external memory handling. We extract sycophancy steering directions from 100 paired prompts and evaluate four open-weight models across 10 steering coefficients and five memory-defense configurations on MemSyco-Bench (answers for all 1,550 items; defense conditions judged on a fixed 250-item subsample), with three LLM judges. Three of the five configurations are new (rewriting every memory, a Router Gate that keeps, rewrites, or drops each memory, and dropping all memory); the other two are MemSyco's baselines. Selective Router Gate filtering preserves substantially more of MemSyco's average accuracy than complete memory removal, and this separation persists when the models are steered toward sycophancy. On Llama 3.1 8B with Router Gate, mild inverse steering ($α= -1.5$) lowers judge-averaged sycophancy from 35.80% to 31.32% while average accuracy moves from 43.99% to 43.31%; this reduction has the same direction under all three judges but is not statistically significant (paired $p = 0.08$ to $0.63$ on 149 items). External memory filtering is the part of the design that holds up; our data do not show that inverse steering adds to it.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
