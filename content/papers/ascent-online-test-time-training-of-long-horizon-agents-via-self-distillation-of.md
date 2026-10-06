# ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05303v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Haodong Lu, Dong Gong
- Tags: agent, context, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.05303v1

## One-Sentence Summary
A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination.

进一步看，论文的核心做法或实验重点可以概括为：Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG

## Abstract Snapshot
A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it. We study Online Agentic Test-Time Training (OaTTT), which trains the LLM's weights on its own execution trajectories during deployment. The agent executes each task once, in one pass over the stream, and the executed trajectory with its verification result is the only learning signal for weight updates that persist across tasks. Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy. We introduce ASCENT (Agentic Self-distillation for Cross-task EvolutioN at Test-time), which instead self-distills verified experience. A stable version of the LLM, its frozen initial copy, receives the verified trajectory as privileged information and predicts next-token distributions along it with this hindsight. Distilling them into persistent LoRA fast weights updates the agent for later tasks, without an external reference solution or stronger teacher. By further removing invalid-action turns, ASCENT distills enhanced privileged experience for more efficient execution. We characterize its population target and the limits of sparse outcome selection. Across ALFWorld, WebShop, and AppWorld at varied model scales, ASCENT improves task success and interaction efficiency as experience accumulates, outperforms online adaptation methods, and transfers to held-out scenes, showing that an agent can consolidate verified experience into its weights without a separate training phase or memory retrieval. Project page: https://artificer-ai-lab.github.io/ASCENT

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
