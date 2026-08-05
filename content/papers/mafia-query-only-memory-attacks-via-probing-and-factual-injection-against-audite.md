# MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.03844v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Jiaming Chen, Yisen Gao, Yanping Li, Zifan Liu, Yumeng Zhang, Jun Zhang
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.03844v1

## One-Sentence Summary
Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats...

进一步看，论文的核心做法或实验重点可以概括为：However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiveness and rigorous semantic checks. To overcome these limitations, we propose MAFIA, a query-only Memory Attack framework via probing and Factual Injection against Audit, tailored to this extended threat model. Specifically, MAFIA introduces: (1) a placement strategy that ensures retrieval-competitive injection via memory probing, budget allocation, and scheduling; and (2) a payload design that bypasses audits using compact factual cloaks, preserving malicious effects while maintaining high semantic similarity. Extensive evaluations reveal that MAFIA achieves up to a 90.7% attack success rate while suppressing audit detection from a peak of 83.3% to at most 7.4%, exposing critical vulnerabilities across agentic memory systems. Code will be made publicly available at https://github.com/JiamingChen1234/MAFIA.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
