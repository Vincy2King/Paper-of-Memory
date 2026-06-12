# SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12703v1
- Published: 2026-06-10
- Updated: 2026-06-10
- Authors: Tarun Sharma
- Tags: agent, retrieval
- Categories: cs.CR, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2606.12703v1

## One-Sentence Summary
Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions.

进一步看，论文的核心做法或实验重点可以概括为：This creates a new attack surface: an adversary interacting only through normal channels can inject crafted memories that, once retrieved, steer the agent's responses for future users, without touching model weights...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI, cs.LG

## Abstract Snapshot
Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions. This creates a new attack surface: an adversary interacting only through normal channels can inject crafted memories that, once retrieved, steer the agent's responses for future users, without touching model weights or code. We call this Multi-Session Memory Poisoning (MSMP) and show that no existing defence certifies against it; static-corpus defences (RobustRAG, ReliabilityRAG) assume a fixed knowledge base, and heuristic filters are bypassed by fluent enterprise-style text. We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting. Component 1 adds HMAC-SHA256 provenance at write time, blocking unsigned injection. Component 2 applies randomised memory ablation with verdict-based majority voting at query time, bounding the influence of authenticated adversaries. We prove that no provenance-free retrieval-time filter can certify against adaptive injection, derive a hypergeometric certificate for Component 2, and formalise the Consistent Minority Effect, whereby a consistent adversarial answer wins string-based voting as a numerical minority while verdict-based voting removes it. Across 15 enterprise scenarios (3,150 repeated trials), Component 1 cuts attack success from 93-100% to 0% for all unsigned variants. For an authenticated adversary with a single injection, Component 2 holds success to 8.0% (95% CI [5.8, 10.9], n=450), below the certified worst case. In an end-to-end query-only attack where the agent itself writes the poison rather than it being pre-seeded, SMSR reduces success from 65.3% to 5.3% (n=150, non-overlapping CIs) on a live agent stack. Clean-query utility is 90% (Component 1) and 85% (combined).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
