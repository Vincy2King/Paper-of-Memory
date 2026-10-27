# FlexA-Mem: Budget-Adaptive Agentic Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.33274v1
- Published: 2026-10-23
- Updated: 2026-10-23
- Authors: Wujiang Xu, Jiaojiao Han, Xi Zhu, Qizheng Zhang, Kaiqu Liang, Yutong Yin, Kai Mei, Dimitris N. Metaxas
- Tags: agent, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.33274v1

## One-Sentence Summary
Large language model (LLM) agents work in scenarios with very different memory needs.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents work in scenarios with very different memory needs.

进一步看，论文的核心做法或实验重点可以概括为：A question about past conversations needs the exact facts it names, while a multi-step task needs a trace of the steps already taken together with details that the next step cannot name.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language model (LLM) agents work in scenarios with very different memory needs. A question about past conversations needs the exact facts it names, while a multi-step task needs a trace of the steps already taken together with details that the next step cannot name. Existing memories are each designed and tested for one kind of scenario. Retrieval memories such as A-Mem miss steps that the current query does not express, summaries drop exact strings, and pairing the two fixes the split of the budget in advance. We propose FlexA-Mem, a general memory that writes each unit of history once into an immutable store and renders a fresh memory for every call. The rendered memory is a compact timeline of records plus detail that a fixed rule fits into the remaining room without an LLM call. The detail is either relevant units as raw text or excerpts or the verbatim pieces that best match the query. With one store, FlexA-Mem serves both kinds of scenario. On AppWorld challenge tasks at 4k, it outperforms the second-best method by 11.5%, and on 147 unused tasks with predictions fixed in advance it outperforms A-Mem with a summary by 12.2%. On LongMemEval and LoCoMo, it matches a dedicated keyword retriever that writes no memory, while memories built on text written by an LLM fall far behind at tight budgets. Ablations show that the timeline carries AppWorld completion, whereas recovery mainly saves steps there and decides accuracy on exact facts. Code is available at https://github.com/WujiangXu/Flex-Amem

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
