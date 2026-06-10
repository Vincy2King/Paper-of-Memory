# REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10694v1
- Published: 2026-06-09
- Updated: 2026-06-09
- Authors: Keer Lu, Liwei Chen, Guoqing Jiang, Zhiheng Qin, Yunhuai Liu, Wentao Zhang
- Tags: context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.10694v1

## One-Sentence Summary
Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons.

进一步看，论文的核心做法或实验重点可以概括为：However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyond the context limit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons. However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyond the context limit. Although recent memory systems attempt to address this issue by storing historical information externally, existing approaches suffer from three key limitations: flat text-based memory organizations fail to capture explicit relations among memories, structured memory systems often destructively overwrite evolving facts, and current retrieval mechanisms remain query-agnostic and passive when evidence is incomplete. REAL constructs long-term conversational memory as a temporal and confidence-aware directed property graph, where each atomic fact is represented with entities, relations, valid-time intervals, confidence scores, and exploration intent labels. During memory construction, REAL adopts a non-destructive temporal update strategy that preserves parallel fact versions and their validity intervals, enabling faithful tracking of fact evolution. During retrieval, REAL anchors query-relevant root entities, decouples their exploration intents, and performs semantic evaluator-guided hybrid beam search to extract compact memory subgraphs. It further incorporates counterfactual inference to repair unreliable retrieval states and recover missing memory evidence through implicit logical relations. Comprehensive experiments demonstrate that REAL substantially improves long-term memory performance over flat-text, graph-based, and existing memory baselines, achieving an average improvement of 22.72\%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
