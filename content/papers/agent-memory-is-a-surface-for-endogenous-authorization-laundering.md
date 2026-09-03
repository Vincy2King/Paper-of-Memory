# Agent Memory Is a Surface for Endogenous Authorization Laundering

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.01836v1
- Published: 2026-09-01
- Updated: 2026-09-01
- Authors: Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol
- Tags: agent
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2609.01836v1

## One-Sentence Summary
Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations.

进一步看，论文的核心做法或实验重点可以概括为：When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks. We term this failure endogenous authorization laundering, where spurious permissions written into memory lead to unauthorized actions as their provenance is washed away. We then introduce EAL-Bench, which measures how accurately persistent memory preserves evolving authorization state and whether errors propagate to downstream unauthorized actions. We evaluate five LLMs as memory writers and two as executors across procurement, cybersecurity, and finance. We find that under incremental memory updates, writers create false authority for up to 50.2% of unauthorized requests; once false authority is present, executors act on it in 98.6% of trials. Two safeguards, requiring stored permissions to be backed by valid source events, and tracking permission changes through bounded event sourcing, substantially reduce laundering, but both also reject more legitimate actions, exposing a safety-utility tradeoff. Persistent memory is therefore not merely a performance component, but a part of an LLM agent's effective authorization policy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
