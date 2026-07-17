# LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.30005v3
- Published: 2026-06-29
- Updated: 2026-07-16
- Authors: Binyan Xu, Haitao Li, Kehuan Zhang
- Tags: agent, compression, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.30005v3

## One-Sentence Summary
Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window.

进一步看，论文的核心做法或实验重点可以概括为：Recent systems make context management agent- or system-controlled, but they either learn a compression policy that discards evidence or manage context in a layer the agent never sees.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window. Recent systems make context management agent- or system-controlled, but they either learn a compression policy that discards evidence or manage context in a layer the agent never sees. We argue both leave a more basic gap unaddressed. Frontier language models are proprioceptively blind to their own context. From the prompt alone they cannot see how large, how old, or how used each block is, the signals a keep-or-drop decision needs. We hypothesize that competent context management is already latent in capable models, and that what is missing is not a learned policy but an interface exposing this state. We introduce VISTA (Visible Internal State for Tool Agents), a training-free, model-agnostic layer that represents working memory as typed, addressable blocks, surfaces a runtime dashboard of per-block token usage, recency, and access history, and archives blocks as recoverable full-fidelity payloads. On LOCA-Bench, BrowseComp-Plus, and GAIA, the same untrained interface transfers across 1M-, 100K-, and 10K-scale trajectories. On LOCA-Bench it improves four backbones and lifts Gemini-3-Flash from 22.7 to 50.7%. The lift grows with context pressure and transfers across backbones. Ablations further confirm that the dashboard matters beyond archive and recovery tools.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
