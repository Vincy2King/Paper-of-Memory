# Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.06956v2
- Published: 2026-11-03
- Updated: 2026-11-06
- Authors: Tianming Sha, Junnan Li, Siqi Zhao
- Tags: agent, context, retrieval
- Categories: cs.LG, cs.CL
- URL: http://arxiv.org/abs/2611.06956v2

## One-Sentence Summary
Deep search and long-horizon reasoning unfold as branching trajectories that pursue parallel sub-queries, abandon dead-end detours, and cross-check sibling findings.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deep search and long-horizon reasoning unfold as branching trajectories that pursue parallel sub-queries, abandon dead-end detours, and cross-check sibling findings.

进一步看，论文的核心做法或实验重点可以概括为：Yet modern serving engines, harnesses, and RL trainers execute episodes as flat, append-only sequences: stretching a context window leaves failed detours that dilute attention, in-place edits break KV caching and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.CL

## Abstract Snapshot
Deep search and long-horizon reasoning unfold as branching trajectories that pursue parallel sub-queries, abandon dead-end detours, and cross-check sibling findings. Yet modern serving engines, harnesses, and RL trainers execute episodes as flat, append-only sequences: stretching a context window leaves failed detours that dilute attention, in-place edits break KV caching and recurrent states, and all-layer cache splicing overwrites hybrid recurrent working memory and triggers hijacking. We introduce Octopus, a co-designed serving runtime, memory manager, and RL framework executing episodes as a GPU-resident DAG over radix cursors (89.6% KV hit rate). Agents coordinate via five primitives: fork shares parent KV prefixes in $O(1)$ with isolated 32K budgets, rewind restores recurrent checkpoints, read_thread mounts sibling KV pages in zero copy, and wait and done synchronize results. Octopus splices sibling KV pages only into full-attention layers under monotonic position offsets while recurrent layers skip mounted spans, retaining 92.2% of full-text answer information and cutting hijacking $21\times$ ($57.9\% \to 2.7\%$) with zero new KV pages. During RL, our packed DAG kernel and DAG-GRPO objective deduplicate shared prefixes via loss masks while keeping mounted KV edges differentiable, cutting rollout-training KL divergence $32\times$ and routing reader gradients into producer KV projections. Trained on Qwen3.5-4B with binary rewards, Octopus self-organizes a commander-worker hierarchy and latent KV mesh, lifting BrowseComp-Plus accuracy under BM25 from 26.0% (32K ReAct) and 32.1% (143K GRPO) to 49.6% (+17.5 pts; 51.2% on OpenResearcher), surpassing 9B context-editing RL (42.5%), matching o3 (49.3%), and outperforming dense-retrieval agents up to $250\times$ larger: Tongyi-DeepResearch (44.5%), DeepSeek-R1 (16.4%), Kimi-K2 (35.4%), GPT-4.1 (36.4%), and Claude 4 Opus (36.8%).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
