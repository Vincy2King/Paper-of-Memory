# TransMem: Transition-Aware Retrieval for Evolving Personal Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.10683v1
- Published: 2026-11-07
- Updated: 2026-11-07
- Authors: Shigeng Chen, Linhao Luo, Changlong Shi, Zhangchi Qiu, Shirui Pan
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.10683v1

## One-Sentence Summary
Long-term personalized agents are increasingly expected to answer queries over user histories in which preferences, goals, and constraints evolve across interleaved conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term personalized agents are increasingly expected to answer queries over user histories in which preferences, goals, and constraints evolve across interleaved conversations.

进一步看，论文的核心做法或实验重点可以概括为：Existing retrieval-based and structured-memory systems can surface relevant facts, but often return isolated memory units that do not explain which earlier preference was refined, contradicted, or superseded by later...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term personalized agents are increasingly expected to answer queries over user histories in which preferences, goals, and constraints evolve across interleaved conversations. Existing retrieval-based and structured-memory systems can surface relevant facts, but often return isolated memory units that do not explain which earlier preference was refined, contradicted, or superseded by later evidence. We introduce TransMem, a transition-aware memory retrieval framework that stores preference updates as explicit retrieval units alongside ordinary factual memories. During memory construction, TransMem routes user interaction history into topic-structured memory graphs, detects shift events, and grounds them as transition records. At inference time, TransMem first retrieves factual anchors and then adaptively expands over transition records, producing a compact context of factual anchors and accepted transition records. Experiments on PersonaMem and PersonaBench across two Qwen backbones show that TransMem outperforms representative retrieval-based and structured-memory baselines. Controlled analyses further show that transition records and adaptive expansion contribute beyond factual anchoring, chronological expansion, flat transition retrieval, and fixed-hop traversal. These results suggest that preference-update records are useful retrieval units for long-term personalization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
