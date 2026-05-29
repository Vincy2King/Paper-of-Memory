# Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30159v1
- Published: 2026-05-28
- Updated: 2026-05-28
- Authors: Ziyan Liu, Zhezheng Hao, Yeqiu Chen, Hong Wang, Jingren Hou, Ruiyi Ding, Yongkang Yang, Wence Ji, Wei Xia, Feng Liu
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.30159v1

## One-Sentence Summary
Memory-augmented LLM agents tackle complex long-horizon tasks by recursively summarizing interaction trajectories into compact memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents tackle complex long-horizon tasks by recursively summarizing interaction trajectories into compact memory.

进一步看，论文的核心做法或实验重点可以概括为：However, existing approaches typically train these memory policies using outcome-based reinforcement learning, failing to localize where intermediate memory quality degrades.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented LLM agents tackle complex long-horizon tasks by recursively summarizing interaction trajectories into compact memory. However, existing approaches typically train these memory policies using outcome-based reinforcement learning, failing to localize where intermediate memory quality degrades. As interactions unfold, ambiguous recursive summaries progressively discard task-relevant information and introduce semantic noise. This exacerbates belief deviation, obscuring the agent's estimate of the latent task state and ultimately derailing long-horizon reasoning. We therefore argue that memory optimization should focus not merely on trajectory-level success, but on the clarity of the belief induced by intermediate summaries. To this end, we introduce Belief Entropy, a self-supervised proxy that probes how uncertain the model remains about the latent task state given its current memory. Based on this proxy, we propose Metacognitive Memory Policy Optimization (MMPO). Instead of relying only on sparse outcome-based signals, MMPO provides fine-grained, memory-specific supervision via explicitly penalizing summaries that induce high epistemic uncertainty. Experiments show that MMPO consistently outperforms existing methods on diverse long-horizon tasks, maintaining 97.1% performance even when scaled to 1.75M-token contexts.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
