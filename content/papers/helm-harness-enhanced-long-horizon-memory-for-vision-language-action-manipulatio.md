# HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.18791v1
- Published: 2026-04-20
- Updated: 2026-04-20
- Authors: Zijian Zeng, Fei Ding, Huiming Yang, Xianwei Li
- Tags: context, episodic
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2604.18791v1

## One-Sentence Summary
Vision-Language-Action (VLA) models fail systematically on long-horizon manipulation tasks despite strong short-horizon performance.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-Language-Action (VLA) models fail systematically on long-horizon manipulation tasks despite strong short-horizon performance.

进一步看，论文的核心做法或实验重点可以概括为：We show that this failure is not resolved by extending context length alone in the current reactive execution setting; instead, it stems from three recurring execution-loop deficiencies: the memory gap, the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Vision-Language-Action (VLA) models fail systematically on long-horizon manipulation tasks despite strong short-horizon performance. We show that this failure is not resolved by extending context length alone in the current reactive execution setting; instead, it stems from three recurring execution-loop deficiencies: the memory gap, the verification gap, and the recovery gap. We present HELM, a model-agnostic framework that addresses these deficiencies with three components: an Episodic Memory Module (EMM) that retrieves key task history via CLIP-indexed keyframes, a learned State Verifier (SV) that predicts action failure before execution from observation, action, subgoal, and memory-conditioned context, and a Harness Controller (HC) that performs rollback and replanning. The SV is the core learning contribution: it consistently outperforms rule-based feasibility checks and ensemble uncertainty baselines, and its effectiveness depends critically on access to episodic memory. On LIBERO-LONG, HELM improves task success rate by 23.1 percentage points over OpenVLA (58.4% to 81.5%), while extending the context window to H=32 yields only a 5.4-point gain and same-budget LoRA adaptation remains 12.2 points below HELM. HELM also improves long-horizon performance on CALVIN and substantially boosts recovery success under controlled perturbations. Ablations and mechanism analyses isolate the contribution of each component, and we release LIBERO-Recovery as a perturbation-injection protocol for evaluating failure recovery in long-horizon manipulation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
