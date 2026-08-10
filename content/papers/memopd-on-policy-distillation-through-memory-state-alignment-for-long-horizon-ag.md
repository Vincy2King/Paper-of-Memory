# MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07068v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Zhiyuan Liu, Tinghong Ye, Chenghao Liu, Yizhuo Li, Songfang Huang
- Tags: agent, compression, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.07068v1

## One-Sentence Summary
Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability.

进一步看，论文的核心做法或实验重点可以概括为：Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations. Learning what to retain typically relies on proximal policy optimization (PPO) with final task rewards, but sparse rewards provide little guidance for individual memory updates. This limitation motivates on-policy distillation (OPD), which supplies dense teacher supervision on student rollouts. For such supervision to be valid, the teacher must evaluate each sampled action under the same state in which it was generated. However, the context rewriting performed during memory compression can break this alignment. When sampled responses are retained and re-encoded for later invocations, flattening the interaction into a persistent history may cause the teacher to score the action under a state that the student never visited during rollout. The action therefore remains on-policy by provenance, but not necessarily by state. We therefore propose Memory-Aligned On-Policy Distillation (MemOPD). MemOPD records the inputs and sampled outputs of each model invocation, restores its original token positions and causal visibility, and packs the reconstructed invocations for efficient teacher scoring. The teacher provides full-vocabulary supervision at the sampled action positions, while PPO preserves the final task objective. Experiments verify state alignment across several context updates and show that it improves F1 by 7.0% over persistent-history teacher scoring in a matched control. Overall, MemOPD-3B improves F1 over PPO by up to 416.2%, while packing yields up to a 1.63x speedup in actor computation during training. The code for this work is publicly available at: https://github.com/TPssp/MemOPD.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
