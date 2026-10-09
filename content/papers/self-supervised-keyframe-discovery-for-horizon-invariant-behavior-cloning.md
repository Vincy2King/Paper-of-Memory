# Self-Supervised Keyframe Discovery for Horizon-Invariant Behavior Cloning

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.10857v1
- Published: 2026-10-07
- Updated: 2026-10-07
- Authors: Prabin Kumar Rath, Omkar Patil, Nakul Gopalan
- Tags: benchmark, context, long-term
- Categories: cs.AI, cs.RO
- URL: http://arxiv.org/abs/2610.10857v1

## One-Sentence Summary
Behavior cloning (BC) in non-Markovian environments is a challenging problem because policies have to reason over contextual information over long horizons.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Behavior cloning (BC) in non-Markovian environments is a challenging problem because policies have to reason over contextual information over long horizons.

进一步看，论文的核心做法或实验重点可以概括为：Existing policy architectures rely on recurrent or attention-based mechanisms to capture long-term dependencies.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, long-term
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.RO

## Abstract Snapshot
Behavior cloning (BC) in non-Markovian environments is a challenging problem because policies have to reason over contextual information over long horizons. Existing policy architectures rely on recurrent or attention-based mechanisms to capture long-term dependencies. However, recurrent models suffer from hidden-state collapse and gradient instability under backpropagation through time, while attention-based models are fundamentally limited by context length. To address these issues, we propose Keyframe Mnemonics, a novel self-supervised method that $\textit{discovers}$ a set of information-critical observations ($\textit{mnemonics}$) by learning an objective from randomly sampled past observations and using it as a reward for keyframe selection. We then train a BC policy that conditions on the discovered keyframes to model the action distribution. Under certain task-structure assumptions, our formulation provides context retention guarantees over an infinite horizon, while maintaining a small set of decision-relevant keyframes in the policy's working memory. We evaluate our method on synthetic memory domains, where mnemonic-conditioned BC policies achieve $100$% success rates (SR) and generalize to horizons orders of magnitude beyond training without performance degradation. Additionally, we evaluate on memory-intensive robot manipulation benchmark, achieving a $13.9$% average absolute SR improvement over the strongest baseline across $23$ tasks and retaining $80$% SR at $20\times$ longer horizons on a real robot. Code and videos are available at https://keyframe-mnemonics.github.io.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
