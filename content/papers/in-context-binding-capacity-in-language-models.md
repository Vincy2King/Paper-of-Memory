# In-Context Binding Capacity in Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.30634v1
- Published: 2026-09-24
- Updated: 2026-09-24
- Authors: Manas Venkata Sai Ravulapalli, Samrath Singh Chadha
- Tags: context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2609.30634v1

## One-Sentence Summary
How many assignments can a language model recall before it loses track of which value belongs to which entity?

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：How many assignments can a language model recall before it loses track of which value belongs to which entity?

进一步看，论文的核心做法或实验重点可以概括为：We measure this limit using continuous recall curves for 12 models at or below 3B parameters and a threshold sweep over 30 open models up to 12B.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.LG

## Abstract Snapshot
How many assignments can a language model recall before it loses track of which value belongs to which entity? We measure this limit using continuous recall curves for 12 models at or below 3B parameters and a threshold sweep over 30 open models up to 12B. On the continuous curves, the load at which recall falls halfway to chance follows $K_{50}=cN^α$, with $α=0.820$ and $R^2=0.73$. The broader sweep shows an eightfold range associated with pretraining recipe, although the continuous curves show no detectable recipe effect after controlling for scale, with few modern models in the fit. We derive why interference can lower measured capacity by reducing single-binding recall even when the load-dependent recall profile is unchanged. Direct task training also exceeds the extrapolated zero-shot law, but different measurement criteria prevent interpreting that comparison as a capacity gain. Its formation times follow a power-law form in two independent codebases, conditional on runs that succeed. Together, these results characterize capacity at the model's query interface. Bounds on joint recall and a decomposition of policy errors connect this measurement to working memory and instruction following, without treating recall as a measure of alignment. The controlled task also provides a baseline for testing whether binding limits constrain world-state tracking; the present experiments do not measure state updates or downstream transfer.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
