# Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.29144v1
- Published: 2026-09-24
- Updated: 2026-09-24
- Authors: Yezhou Cheng, Runjia Du, Zeming Liu, Qibai Chen, Hang Lyu, Yankai Zeng, Yilan Wei, Bojun Lin
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.29144v1

## One-Sentence Summary
Persistent memory lets language-model agents improve prompts and skills without updating model weights.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory lets language-model agents improve prompts and skills without updating model weights.

进一步看，论文的核心做法或实验重点可以概括为：We show that matching retrieval scope to certification scope enables these edits to support reliable repeated adaptation across recurring task families.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory lets language-model agents improve prompts and skills without updating model weights. We show that matching retrieval scope to certification scope enables these edits to support reliable repeated adaptation across recurring task families. We study frozen-model agents on ProcStream-RSI, a 12-round code-repair stream, using Orthogonal Regression Control (ORC), an execution-grounded gate for persistent skill edits. In an intervention that holds proposals and gate decisions fixed, retrieving each accepted skill only for its originating family raises mean hidden trajectory utility from 0.713 under global memory to 0.816 and changes harmful deployments from six of eight to none. In 27 paired randomized-order streams, Scoped-ORC improves mean trajectory utility by 0.063 [0.037, 0.094] over Global-ORC, accepts 63 rather than 12 updates, and produces multiple accepted updates in 19/27 streams, with 0/63 harmful acceptances. The global control reaches 0.713, below the static agent's 0.775, because locally valid edits can interfere with unrelated families. These results establish scope matching as a complementary control for persistent agent memory: certification determines whether an edit is supported, while retrieval scope determines where that evidence authorizes its use.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
