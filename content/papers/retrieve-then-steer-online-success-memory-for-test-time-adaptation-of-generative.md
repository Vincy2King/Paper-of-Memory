# Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.10094v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Jianchao Zhao, Huoren Yang, Hu Yusong, Yuyang Gao, Qiguan Ou, Cong Wan, SongLin Dong, Zhiheng Ma, Yihong Gong
- Tags: long-term, retrieval
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2605.10094v1

## One-Sentence Summary
Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment...

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment conditions.

进一步看，论文的核心做法或实验重点可以概括为：Existing evaluations typically treat test episodes as independent zero-shot trials.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment conditions. Existing evaluations typically treat test episodes as independent zero-shot trials. However, real robots often operate repeatedly in the same or slowly changing environments, where successful executions provide environment-verified evidence of reliable behavior patterns. We study this persistent-deployment setting, asking whether a partially competent frozen VLA can improve its reliability by reusing its successful test-time experience. We propose an online success-memory guided test-time adaptation framework for generative VLAs. During deployment, the robot stores progress-calibrated successful observation-action segments in a long-term memory. At inference, it retrieves state-relevant action chunks, filters inconsistent candidates via trajectory-level consistency, and aggregates them into an elite action prior. To incorporate this prior into action generation, we introduce confidence-adaptive prior guidance, which injects the elite prior into an intermediate state of the flow-matching action sampler and adjusts the guidance strength based on retrieval confidence. This design allows the frozen VLA to exploit environment-specific successful experience while preserving observation-conditioned generative refinement. This retrieve-then-steer mechanism enables lightweight, non-parametric test-time adaptation without requiring parameter updates. Simulation and real-world experiments show improved task success and closed-loop stability, especially in long-horizon and multi-stage tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
