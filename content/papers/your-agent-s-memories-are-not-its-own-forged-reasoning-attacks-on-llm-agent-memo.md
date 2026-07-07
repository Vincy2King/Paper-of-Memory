# Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.05029v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu, Dinghao Wu
- Tags: agent, context
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2607.05029v1

## One-Sentence Summary
Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context.

进一步看，论文的核心做法或实验重点可以概括为：While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
