# SkillGrad: Optimizing Agent Skills Like Gradient Descent

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.27760v1
- Published: 2026-05-26
- Updated: 2026-05-26
- Authors: Hanyu Wang, Yifan Lan, Bochuan Cao, Lu Lin, Jinghui Chen
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.27760v1

## One-Sentence Summary
Agent skills provide a lightweight way to adapt LLM agents to specialized domains by storing reusable procedural knowledge in structured files.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent skills provide a lightweight way to adapt LLM agents to specialized domains by storing reusable procedural knowledge in structured files.

进一步看，论文的核心做法或实验重点可以概括为：However, whether downloaded from third parties or self-generated, these skills are often unreliable, incomplete, or outdated.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Agent skills provide a lightweight way to adapt LLM agents to specialized domains by storing reusable procedural knowledge in structured files. However, whether downloaded from third parties or self-generated, these skills are often unreliable, incomplete, or outdated. Existing skill-evolution methods often address these deficiencies through heuristic reflections without an explicit optimization formulation. In this paper, we propose SkillGrad, a gradient-descent-inspired framework for optimizing agent skills. SkillGrad treats the skill package as a structured parameter to optimize in a gradient descent fashion: task executions provide trajectory-level loss evidence, automatic diagnoses then provide text-based gradients that indicate the correction directions. To stabilize optimization across iterations, a momentum agent accumulates recurring diagnostic patterns into a persistent memory overlay. Finally, an LLM-based patcher executes the parameter update by applying layer-aware edits to the skill package. Evaluated on SpreadsheetBench Verified and WikiTableQuestions, SkillGrad consistently outperforms training-based skill evolution baselines across two backbone LLMs, improving over the strongest training-based baseline by $6.7$ percentage points on average. Ablations further show that momentum and contrastive diagnosis both contribute to the final skill quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
