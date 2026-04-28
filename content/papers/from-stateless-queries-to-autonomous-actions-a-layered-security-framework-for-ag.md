# From Stateless Queries to Autonomous Actions: A Layered Security Framework for Agentic AI Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.23338v1
- Published: 2026-04-25
- Updated: 2026-04-25
- Authors: Kexin Chu
- Tags: agent, benchmark, long-term
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2604.23338v1

## One-Sentence Summary
Agentic AI systems face security challenges that stateless large language models do not.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic AI systems face security challenges that stateless large language models do not.

进一步看，论文的核心做法或实验重点可以概括为：They plan across extended horizons, maintain persistent memory, invoke external tools, and coordinate with peer agents.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
Agentic AI systems face security challenges that stateless large language models do not. They plan across extended horizons, maintain persistent memory, invoke external tools, and coordinate with peer agents. Existing security analyses organize threats by attack type (prompt injection, jailbreaking), but provide no principled model of which architectural component is vulnerable or over what timescale the threat manifests. This paper makes five contributions. First, we introduce the Layered Attack Surface Model (LASM), a seven-layer framework that maps threats to distinct architectural components: Foundation, Cognitive, Memory, Tool Execution, Multi-Agent Coordination, Ecosystem, and Governance, the accountability and observability layer that spans the stack analogously to the network management plane. Second, we introduce attack temporality as an orthogonal analytical dimension with four classes: Instantaneous (T1), Session-Persistent (T2), Cross-Session Cumulative (T3), and Sub-Session-Stack, Non-Session-Bounded (T4). Third, through a systematic review of 94 papers (2021--2025), we show that the most dangerous emerging threats concentrate at the intersection of high-layer attacks (L5--L7) and slow-burn temporality (T3--T4): covert agent collusion, long-term memory poisoning, MCP supply-chain compromise, and alignment failure that manifests as an insider threat with no external adversary. Only 8 of 120 paper-cell assignments (7%) fall in this zone. Fourth, we propose a cross-layer defense taxonomy spanning all seven LASM layers and all four temporality classes, exposing which threat classes existing defenses leave unaddressed. Fifth, we survey evaluation benchmarks, identify five research gaps in the under-studied high-layer, slow-burn zone, and argue that agentic security must be treated as a distributed systems problem embedded in an adversarial ecosystem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
