# SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22725v1
- Published: 2026-08-24
- Updated: 2026-08-24
- Authors: Jiaqi Liu, Maolin Ran, Xiaoyang Lu, Jian Wang, Weiwen Liu, Jianghao Lin, Yong Yu, Weinan Zhang
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.22725v1

## One-Sentence Summary
Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck.

进一步看，论文的核心做法或实验重点可以概括为：Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck. Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent. Once assembled, these small discrepancies amplify into severe visual breaks. We present SEAM (Shot Entity-Attribute Memory), a training-free, model-agnostic memory graph that repairs continuity entirely at the prompt-text layer by extracting a multi-dimensional state for every shot, retrieving only causally prior context over the resulting graph, filtering it selectively, and injecting the surviving constraints by natural-language prompt rewriting. We further release SEAM-Bench, a double-blind continuity storyboarding benchmark, on which SEAM raises cross-episode continuity recall from 0.700 to 0.946, generalizes across six mainstream text models, and yields consistent, though not yet significant, gains at the generated-image layer. Deployed as a mandatory stage in CreativeFitting's SEAM-Agent production pipeline over 201 shots, SEAM reaches a 96.5% director-acceptance rate with zero unsafe injections; a conservative counterfactual attributes at least 21.9 percentage points of that rate to its cross-episode memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
