# When Context Changes: Understanding Update Failures in LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38866v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Junyu Guo, Yuchen Fang, Shangding Gu, Costas Spanos, James Demmel, Javad Lavaei
- Tags: agent, benchmark, context, conversation
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.38866v1

## One-Sentence Summary
As preferences, goals, and facts change, LLM agents must use the current state while earlier versions remain in context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As preferences, goals, and facts change, LLM agents must use the current state while earlier versions remain in context.

进一步看，论文的核心做法或实验重点可以概括为：Yet they can answer with an old value of the same variable, a failure that we call stale binding.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation
- 检索关键词命中：context memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As preferences, goals, and facts change, LLM agents must use the current state while earlier versions remain in context. Yet they can answer with an old value of the same variable, a failure that we call stale binding. To study when models use outdated information and why, we introduce Controlled In-Context Memory (CICM), a benchmark for tracking and using updated information in conversations and agent logs. We observe that even frontier reasoning models can fail to recover the current state. We find that in open-source models probes can still recover the updated value when the model answers with an old one, pointing to a failure to select information that remains available. Component tests in Qwen and Pythia identify a mechanism for this selection failure: attention drift, where attention favors old values over the current one when producing an answer. We study a one-layer transformer to mathematically understand how this phenomenon happens: when attention scores are similar, several old values can together receive more attention than the current value. Guided by this explanation, we redirect attention toward the current value without further training. When the current value is requested directly, adjusting this intervention for each input corrects most old-value errors across various model families while preserving nearly all initially correct answers. Reliable context management therefore requires more than remembering updated information: models must use it to guide their answers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
