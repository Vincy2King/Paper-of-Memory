# AgentWebRec: Compact Evidence Fusion over the Agent Web for Personalized Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.01705v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Haoran Qiang, Guannan Liu, Liang Zhang, Junjie Wu
- Tags: agent
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.01705v1

## One-Sentence Summary
LLM-based personal agents are emerging as persistent carriers of user semantics and intermediaries between users and recommendation platforms, maintaining richer user knowledge...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based personal agents are emerging as persistent carriers of user semantics and intermediaries between users and recommendation platforms, maintaining richer user knowledge locally.

进一步看，论文的核心做法或实验重点可以概括为：As agents interact with one another, the conventional \textit{User--Platform} relation evolves into a \textit{User--Agent Web--Platform} information pathway, enabling distributed user-side information to complement...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.IR

## Abstract Snapshot
LLM-based personal agents are emerging as persistent carriers of user semantics and intermediaries between users and recommendation platforms, maintaining richer user knowledge locally. As agents interact with one another, the conventional \textit{User--Platform} relation evolves into a \textit{User--Agent Web--Platform} information pathway, enabling distributed user-side information to complement item-side information. This new pathway, however, defies conventional recommendation: evidence is scattered across mutually opaque agents and reachable only through bounded queries, only a small portion of it is relevant to the current recommendation decision, and the responses returned by different agents are semantically heterogeneous. We therefore recast recommendation over the agent web as a \emph{task-time evidence acquisition and fusion} problem under a finite evidence budget by deciding what to ask and what to keep, rather than learning from aggregated data. We propose AgentWebRec, a user-agent-oriented framework that progressively acquires and fuses distributed evidence for each user-item decision while keeping underlying agent memories local. It grounds each decision in platform-provided item semantics and task-relevant evidence from the target user agent's private memory, and conditionally queries neighboring user agents for complementary preference patterns when local evidence is insufficient. Experiments on four InstructRec datasets show that AgentWebRec consistently outperforms baseline recommenders, and ablations verify that the evidence layers contribute complementary gains.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
