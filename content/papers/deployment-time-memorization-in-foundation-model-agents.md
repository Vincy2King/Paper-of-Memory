# Deployment-Time Memorization in Foundation-Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10062v1
- Published: 2026-06-08
- Updated: 2026-06-08
- Authors: Lei, Chen, Guilin Zhang, Kai Zhao, Dalmo Cirne, Andy Olsen, Xu Chu, Zeke Miller, Alet Blanken, Amine Anoun, Jerry Ting
- Tags: agent, compression, retrieval
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2606.10062v1

## One-Sentence Summary
Foundation-model agents are increasingly long-lived systems that remember users across interactions, making memorization an explicit deployment-time function rather than solely...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Foundation-model agents are increasingly long-lived systems that remember users across interactions, making memorization an explicit deployment-time function rather than solely a property of model weights.

进一步看，论文的核心做法或实验重点可以概括为：Existing work addresses parametric memorization or audits fixed memory configurations, but does not characterize how memory-design choices jointly shape personalization utility, extraction risk, and deletion fidelity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Foundation-model agents are increasingly long-lived systems that remember users across interactions, making memorization an explicit deployment-time function rather than solely a property of model weights. Existing work addresses parametric memorization or audits fixed memory configurations, but does not characterize how memory-design choices jointly shape personalization utility, extraction risk, and deletion fidelity. We study this surface as deployment-time memorization, formulating agent memory as a privacy-utility frontier measured by Personalization Recall (PR) and Adversarial Extraction Rate (AER), and sweeping three memory-design knobs: summarization aggressiveness, retrieval breadth (k), and deletion mode. We further introduce the Forgetting Residue Score (FRS) to quantify whether deleted information remains recoverable from derived memory tiers. On LongMemEval, key-fact summarization reduces canary extraction by 76% on Gemma 3 12B and 64% on GPT-4o-mini while preserving nearly all personalization recall; critically, once content is compressed away, increasing k no longer restores leakage. The same compression, however, induces a deletion-fidelity failure: raw-only deletion leaves derived summary copies recoverable in approximately 20% of instances, and only full-pipeline purge or tombstone redaction drives worst-tier residue to zero. Together, these results establish that persistent agent memory must be evaluated as a first-class memorization mechanism -- assessed by what it helps agents recall, what it makes extractable, and what it can truly erase.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
