# EviGraph: Towards Verifiable Evidence Construction for Information-Seeking Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.24667v1
- Published: 2026-08-25
- Updated: 2026-08-25
- Authors: Jiashun Chen, Yirong Mao, Wenhui Que
- Tags: agent
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.24667v1

## One-Sentence Summary
Agentic Web search can retrieve relevant information without establishing that the retrieved content actually supports the claims used in an answer.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic Web search can retrieve relevant information without establishing that the retrieved content actually supports the claims used in an answer.

进一步看，论文的核心做法或实验重点可以概括为：Existing agents typically keep search and evidence recording in a linear interaction trace and optimize primarily for final-answer correctness, providing limited supervision for intermediate grounding.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：working memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Agentic Web search can retrieve relevant information without establishing that the retrieved content actually supports the claims used in an answer. Existing agents typically keep search and evidence recording in a linear interaction trace and optimize primarily for final-answer correctness, providing limited supervision for intermediate grounding. We present EviGraph, a deep-search framework that separates search execution from evidence recording while using a shared policy for the trainable roles. An executor plans concise queries, a frozen evidence verifier inspects source pages and returns verbatim evidence items with an explicit polarity, and the policy maps those items to add/support graph requests that are checked by a deterministic structural validator. The resulting graph serves both as persistent working memory and as a source of dense process rewards, enabling reinforcement learning to directly supervise evidence construction rather than only the final answer. On BrowseComp-Plus, a Qwen3-8B EviGraph agent achieves 35.9% accuracy under a matched interaction budget, compared with 26.9% for the same dual-role architecture without reinforcement learning and 2.7% for a monolithic agent, while generating fewer tokens per rollout. Consistent gains on BrowseComp, GAIA, and XBench indicate that explicitly structuring and rewarding evidence recording improves agentic search

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
