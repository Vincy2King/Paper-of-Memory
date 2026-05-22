# LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.22786v1
- Published: 2026-05-21
- Updated: 2026-05-21
- Authors: Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy
- Tags: agent, benchmark, context
- Categories: cs.AI, cs.ET, cs.LG, cs.MA
- URL: http://arxiv.org/abs/2605.22786v1

## One-Sentence Summary
Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks.

进一步看，论文的核心做法或实验重点可以概括为：While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.ET, cs.LG, cs.MA

## Abstract Snapshot
Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque channel through which sensitive content may propagate across agents without explicit textual disclosure. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. LCGuard treats shared KV caches as latent working memory and learns representation-level transformations before cache artifacts are transmitted across agents. We formalize representation-level sensitive information leakage operationally through reconstruction: a shared cache artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation in which the adversary learns to reconstruct sensitive inputs, while LCGuard learns transformations that preserve task-relevant semantics and reduce reconstructable information. Empirical evaluations across multiple model families and multi-agent benchmarks show that LCGuard consistently reduces reconstruction-based leakage and attack success rates while maintaining competitive task performance compared to standard KV-sharing baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
