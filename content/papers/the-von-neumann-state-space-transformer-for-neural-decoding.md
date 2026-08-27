# The Von-Neumann State-Space Transformer for neural decoding

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.25088v1
- Published: 2026-08-25
- Updated: 2026-08-25
- Authors: Morteza Sarafyazd
- Tags: benchmark, context
- Categories: cs.LG, cs.AI, q-bio.NC
- URL: http://arxiv.org/abs/2608.25088v1

## One-Sentence Summary
Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of individual neurons.

进一步看，论文的核心做法或实验重点可以概括为：Our aim is sample efficiency-models that decode well from limited data and at small parameter budgets.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.AI, q-bio.NC

## Abstract Snapshot
Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of individual neurons. Our aim is sample efficiency-models that decode well from limited data and at small parameter budgets. In a standard Transformer layer, the feed-forward block applies the same operator to every token. We suggest a von-Neumann inspired hypothesis of efficient computation as an alternative for neural decoding: a controller decodes an instruction and then executes a token-specific operator; the usual realization-a soft mixture of experts-only blends their outputs, not operators. We introduce a von-Neumann State-Space Transformer (VN-SST), a memory-augmented Transformer whose feed-forward block is a low-rank instruction bank: a shared base operator plus a small set of learned low-rank instructions, from which a per-token code synthesizes the weight matrix actually used at that token. The code is read from a low- dimensional projection of a carried state-space memory, so a slow latent trajectory acts as an instruction pointer-mirroring how low-dimensional dynamics may route cortical computation. On three motor-cortex neural-decoding benchmarks, VN-SST is far more data-efficient than a modern Transformer, each jointly predicting spikes and decoding behavior. This model wins by a wide margin on the scarcest benchmark, leads on the other two, and turns longer context into rising rather than falling accuracy. We evaluated that the network compresses a large instruction bank to a few bits per token, so program capacity acts as a control channel, not an accuracy lever. The same model is also more parameter-efficient on two small text benchmarks used for language modeling (LLMs), suggesting a generic mechanism.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
