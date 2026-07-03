# ElephantAgent: Contextual State Continuity in Agentic Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.01919v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Jiankai Jin, Xiangzheng Zhang, Zhao Liu, Wenzhuo Xu, Dongdong Yang, Deyue Zhang, Quanchen Zou
- Tags: agent, context
- Categories: cs.AI, cs.CR
- URL: http://arxiv.org/abs/2607.01919v1

## One-Sentence Summary
Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory.

进一步看，论文的核心做法或实验重点可以概括为：However, these external dependencies introduce novel attack surfaces.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CR

## Abstract Snapshot
Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory. However, these external dependencies introduce novel attack surfaces. Recent tool and memory poisoning attacks show that maliciously crafted tool descriptors and poisoned memory can covertly bias agent behavior. These threats reflect a deeper issue: the lack of verifiable continuity in the agent's contextual state for planning and execution. We present ElephantAgent, a protocol that enforces Contextual State Continuity to defend against contextual state poisoning. Inspired by prior state-continuity mechanisms (e.g., Nimble), ElephantAgent extends this protection to the evolving contextual state of agentic systems. We define the contextual state as the bounded, security-critical subset of the agent's entire context (e.g., tool state and memory). Before processing each query, ElephantAgent recomputes the digest of the local contextual state and verifies it against the latest authorized digest. Using replicated trusted hardware, ElephantAgent maintains a linearizable ledger of authorized contextual state transitions and detects out-of-band state tampering. To handle in-band semantic abuse, ElephantAgent additionally provides Historical Traceability, enabling conditional post-hoc audit and recovery to a known-good prior state.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
