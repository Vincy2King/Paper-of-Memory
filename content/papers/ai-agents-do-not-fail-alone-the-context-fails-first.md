# AI Agents Do Not Fail Alone:The Context Fails First

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.14275v1
- Published: 2026-07-15
- Updated: 2026-07-15
- Authors: Fouad Bousetouane
- Tags: agent, context
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2607.14275v1

## One-Sentence Summary
Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured.

进一步看，论文的核心做法或实验重点可以概括为：Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured. Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context. When this context is weak, agents drift, hallucinate, misuse tools, ignore constraints, become vulnerable to injection, and waste tokens. This paper validates context-engineering quality as an independent leading indicator of agent reliability. We implement the measurement in ProofAgent-Harness, an open-source infrastructure for AI agent evaluation that uses multi-juror, consensus-based scoring. The harness assesses context across seven criteria: role clarity, guardrail coverage, instruction consistency, tool schema quality, grounding sufficiency, injection hardening, and token efficiency. Crucially, the context score is isolated from behavioral metrics and release decisions, enabling a non-circular validation. Through a controlled context-quality study across regulated agent domains, holding frontier LLM agents fixed and varying only their operating context, we show that context-quality criteria consistently predict their corresponding behavioral outcomes. Grounding sufficiency predicts hallucination resistance, guardrail coverage predicts manipulation resistance, instruction consistency predicts instruction following, and tool-schema quality predicts tool use. These findings establish context measurement as a validated preflight signal for agent reliability and position context engineering as an auditable layer of agent evaluation and governance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
