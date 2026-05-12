# Mem-W: Latent Memory-Native GUI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09317v1
- Published: 2026-05-10
- Updated: 2026-05-10
- Authors: Guibin Zhang, Yaohui Ling, Fanci Meng, Kun Wang, Shuicheng Yan
- Tags: agent, benchmark, context
- Categories: cs.CL, cs.CV, cs.LG
- URL: http://arxiv.org/abs/2605.09317v1

## One-Sentence Summary
GUI agents are beginning to operate the web, mobile, and desktop as interactive worlds, where successful control depends on carrying forward visual, procedural, and task-level...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：GUI agents are beginning to operate the web, mobile, and desktop as interactive worlds, where successful control depends on carrying forward visual, procedural, and task-level evidence beyond the fleeting present screen.

进一步看，论文的核心做法或实验重点可以概括为：Yet most agents still treat memory as an external, human-readable artifact: histories are summarized, categorized, retrieved, and reinserted as text or structured records before being encoded again by the policy.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.CV, cs.LG

## Abstract Snapshot
GUI agents are beginning to operate the web, mobile, and desktop as interactive worlds, where successful control depends on carrying forward visual, procedural, and task-level evidence beyond the fleeting present screen. Yet most agents still treat memory as an external, human-readable artifact: histories are summarized, categorized, retrieved, and reinserted as text or structured records before being encoded again by the policy. This creates a mismatch between the representational form in which experience is stored and the latent embedding sequence over which modern GUI policies actually act. We introduce Mem-W, a series of latent-memory-native GUI agents that treat memory as part of the agent's continuous context rather than as an auxiliary symbolic scaffold. Mem-W weaves both historical trajectories (as experiential memory) and in-session segments (as working memory) into compact memory tokens through a shared trajectory-to-latent compressor. These tokens are woven with the current GUI observation and local context into one continuous embedding sequence, allowing the agent to read successes, failures, and unfinished progress through the same machine-native interface. Mem-W is trained with self-distillation and outcome-aware supervision to preserve decision-relevant state while filtering memory toward evidence that truly supports task success. Across four web and mobile navigation benchmarks, Mem-W consistently improves diverse backbones and memory-enhanced baselines, with gains of up to $+30.0$, suggesting that latent-context-native memory can serve as a scalable foundation for long-horizon GUI agency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
