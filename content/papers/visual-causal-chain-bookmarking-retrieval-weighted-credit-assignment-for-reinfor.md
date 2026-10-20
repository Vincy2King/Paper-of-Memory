# Visual Causal-chain Bookmarking: Retrieval-Weighted Credit Assignment for Reinforcement Learning from Delayed Reward

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.24032v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Prathap Selvakumar
- Tags: agent, episodic, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.24032v1

## One-Sentence Summary
RL agents trained on a single trajectory-level return face a credit-assignment problem: when a reward arrives many steps after the decision that caused it, every action gets the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：RL agents trained on a single trajectory-level return face a credit-assignment problem: when a reward arrives many steps after the decision that caused it, every action gets the same signal regardless of causal...

进一步看，论文的核心做法或实验重点可以概括为：This paper studies Visual Causal-chain Bookmarking (VCBM), which concentrates credit on the decision points that determine an episode's return, via two instantiations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG

## Abstract Snapshot
RL agents trained on a single trajectory-level return face a credit-assignment problem: when a reward arrives many steps after the decision that caused it, every action gets the same signal regardless of causal responsibility. This paper studies Visual Causal-chain Bookmarking (VCBM), which concentrates credit on the decision points that determine an episode's return, via two instantiations. The first targets a fully observed, low-dimensional MDP (a delayed-reward watch-repair task), where VCBM statistically discovers which state components the agent causally controls and estimates per-decision-point action values directly, evaluated against ground truth and RUDDER, an LSTM-based baseline. VCBM converges to 95.07% correct decisions in a mean of 1,532.3 episodes across 20 seeds, versus RUDDER's slower, more variable convergence (mean 3,327.1 episodes; p<0.001); VCBM's discovered causal structure exactly matches ground truth in all seeds. The second targets a partially observed, language-based setting: an LLM agent trained with Leave-One-Out PPO (LOOP) in AppWorld, where causal discovery is intractable and a structural heuristic (state-mutating tool calls) substitutes for it, with credit distributed via retrieval over episodic memory and blended with LOOP's advantage. Over 200 iterations on identical Qwen2.5-7B-Instruct/LoRA/FSDP2 configurations, VCBM-blended LOOP improves task success over plain LOOP (0.354 vs. 0.458), reduces final-step max importance weight, and improves token efficiency, with a small KL exception favouring LOOP. The watch-repair result supports the claim that weighting causally relevant steps is more sample-efficient than an undifferentiated baseline or a learned return-redistribution network; the AppWorld result, limited to one seed per arm by a 2-GPU budget, is a compute-limited demonstration at a harder, natural-language scale, not a statistical confirmation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
