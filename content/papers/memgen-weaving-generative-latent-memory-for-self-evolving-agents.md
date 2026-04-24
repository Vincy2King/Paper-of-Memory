# MemGen: Weaving Generative Latent Memory for Self-Evolving Agents

- Source: OpenReview
- Venue: ICLR 2026 Poster
- Paper ID: openreview:vI56m4Iu4e
- Published: 2026-01-26
- Updated: 2026-04-11
- Authors: Guibin Zhang, Muxin Fu, Shuicheng YAN
- Tags: agent, benchmark, retrieval
- Categories: ICLR.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=vI56m4Iu4e

## One-Sentence Summary
Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing paradigms remain constrained: parametric memory forcibly adjusts model parameters, and retrieval-based memory externalizes experience into structured databases, yet neither captures the fluid interweaving of...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Poster
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, working memory
- 来源分类信息：ICLR.cc/2026/Conference/-/Submission

## Abstract Snapshot
Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions. Existing paradigms remain constrained: parametric memory forcibly adjusts model parameters, and retrieval-based memory externalizes experience into structured databases, yet neither captures the fluid interweaving of reasoning and memory that underlies human cognition. To address this gap, we propose MemGen, a dynamic generative memory framework that equips agents with a human-esque cognitive faculty. It consists of a \textit{memory trigger}, which monitors the agent’s reasoning state to decide explicit memory invocation, and a \textit{memory weaver}, which takes the agent's current state as stimulus to construct a latent token sequence as machine-native memory to enrich its reasoning. In this way, MemGen enables agents to recall and augment latent memory throughout reasoning, producing a tightly interwoven cycle of memory and cognition. Extensive experiments across eight benchmarks show that MemGen surpasses leading external memory systems such as ExpeL and AWM by up to $38.22\\%$, exceeds GRPO by up to $13.44\\%$, and exhibits strong cross-domain generalization ability. More importantly, we find that without explicit supervision, MemGen spontaneously evolves distinct human-like memory faculties, including planning memory, procedural memory, and working memory, suggesting an emergent trajectory toward more naturalistic forms of machine cognition.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
