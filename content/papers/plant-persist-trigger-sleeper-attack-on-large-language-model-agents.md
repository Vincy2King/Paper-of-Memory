# Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.28201v1
- Published: 2026-05-27
- Updated: 2026-05-27
- Authors: Yongxiang Li, Moxin Li, Zhixin Ma, Fengbin Zhu, Dongrui Liu, Wenjie Wang, Fuli Feng
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.28201v1

## One-Sentence Summary
Large Language Model (LLM) agents remain vulnerable to safety threats from the external environment, where attackers inject adversarial content into external observations such...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents remain vulnerable to safety threats from the external environment, where attackers inject adversarial content into external observations such as tool-returned data, webpages, or MCP...

进一步看，论文的核心做法或实验重点可以概括为：Existing studies typically focus on single-interaction attacks, where the agent observes adversarial content and immediately exhibits harmful behavior within one user request.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large Language Model (LLM) agents remain vulnerable to safety threats from the external environment, where attackers inject adversarial content into external observations such as tool-returned data, webpages, or MCP context, causing harmful agentic behaviors such as unsafe actions or incorrect outputs. Existing studies typically focus on single-interaction attacks, where the agent observes adversarial content and immediately exhibits harmful behavior within one user request. However, we show that adversarial content can also persist across interactions served by the same agent, making such threats harder to detect and mitigate. Specifically, adversarial content may persist in the agent state, remain dormant across interactions, and later be activated by a benign user query. We formalize this type of safety threat as Sleeper Attack. To evaluate it, we construct a benchmark with 1,896 instances covering six real-world harmful outcomes, three attack strategies, and three agent state targets: session context, memory, and reusable skills. Experiments on seven strong open-source and closed-source LLMs show that state-of-the-art LLM agents remain vulnerable to Sleeper Attack, even when they achieve low attack success rates under a single-interaction baseline. Our code and data are available at https://anonymous.4open.science/r/skdvnfu23ihr9wdscnksf1asdffsaef.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
