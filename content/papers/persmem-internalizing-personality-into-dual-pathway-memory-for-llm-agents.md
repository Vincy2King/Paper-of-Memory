# PersMem: Internalizing Personality into Dual-Pathway Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34372v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Hanzhong Zhang, Ziwei Xiang, Weicheng Xie, Shizhe Liu, Siyang Song
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.34372v1

## One-Sentence Summary
The profile of a role-playing agent usually depends on the pre-defined personality in a system prompt, whereas its memory processing pipeline, including prioritisation of stored...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The profile of a role-playing agent usually depends on the pre-defined personality in a system prompt, whereas its memory processing pipeline, including prioritisation of stored memories and subsequent retrieval,...

进一步看，论文的核心做法或实验重点可以概括为：This separation causes the agent's memory processing to be inconsistent with the pre-defined personality, and makes it difficult to validate whether agent behaviours follow this personality.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, memory retrieval, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
The profile of a role-playing agent usually depends on the pre-defined personality in a system prompt, whereas its memory processing pipeline, including prioritisation of stored memories and subsequent retrieval, remains independent of this personality. This separation causes the agent's memory processing to be inconsistent with the pre-defined personality, and makes it difficult to validate whether agent behaviours follow this personality. In this paper, we propose Personality-Integrated Memory (PersMem), which integrates personality into the agent's memory processing pipeline, making it consistently personality-dependent. PersMem processes memory using four steps, where the personality is mapped to operation-specific parameters controlling: (i) affective appraisal annotating emotion states of the user input; (ii) retention of previously stored memories along with the current input; (iii) passive affect-driven memory retrieval exploring memories similar to user input in semantics and personality-guided emotions; and (iv) active goal-driven memory retrieval that refines and selects passively retrieved memories for the reply. Consequently, consistency with the pre-defined personality can be examined by inspecting memory-processing traces during human-agent interactions. We evaluate these personality-dependent differences in attachment and Big Five settings. PersMem exceeds the chance baseline for four-way attachment classification by 23.1 percentage points. In Big Five dialogue comparisons, PersMem achieves 67.5% accuracy, 6.7 percentage points above a baseline using uniformly sampled memories. On CoSER, PersMem achieves an average score of 66.13, with scores of 69.33 for Character Fidelity and 84.33 for Storyline Quality. Together, these results show that PersMem produces distinguishable personality-related memory-processing patterns.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
