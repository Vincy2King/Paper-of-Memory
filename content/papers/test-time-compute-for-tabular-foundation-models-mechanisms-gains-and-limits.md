# Test-Time Compute for Tabular Foundation Models: Mechanisms, Gains, and Limits

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.12005v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Kanghui Ning, Marin Biloš, James T. Wilson, Yilang Zhang, Kashif Rasul, Dongjin Song, Anderson Schneider, Yuriy Nevmyvaka
- Tags: benchmark, context, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.12005v1

## One-Sentence Summary
Which forms of test-time compute improve the predictions of strong pretrained tabular foundation models (TFMs)?

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Which forms of test-time compute improve the predictions of strong pretrained tabular foundation models (TFMs)?

进一步看，论文的核心做法或实验重点可以概括为：We systematically study this along three axes: adaptation, aggregation, and context construction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：context memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Which forms of test-time compute improve the predictions of strong pretrained tabular foundation models (TFMs)? We systematically study this along three axes: adaptation, aggregation, and context construction. Our evaluation spans modern TFMs across the TabArena benchmark, supplemented by experiments on wide and large-scale tables from OpenML. For adaptation, we introduce DiagScale, a diagonal query-key similarity update. It trains only 0.003-0.03% of model parameters and achieves gains comparable to full fine-tuning across three independently pretrained backbones. For aggregation, both pool composition and selection strategy matter. TabPFN-3 already averages predictions from different preprocessing variants of the same data, and adding more such predictions yields diminishing returns. With a broader pool of 96 configurations, greedy selection reduces error by 2.4% relative to the default predictor, but uniform averaging increases error. For context construction, attention-guided retrieval improves TabPFN-3's predictions on some large tables and supports source pools beyond the full context memory limit. The context expansion methods we test yield no consistent improvement. Taken together, our results suggest that adaptation and selective aggregation yield consistent benchmark-level gains. The benefits of context construction depend more on the task and data regime. Adaptation and aggregation over the same backbone yield further gains when combined, but require substantially more computation than default inference. These trade-offs motivate choosing strategies according to the available computation budget. Code is available at https://github.com/kanghui-learning/test-time-compute-for-tabular-foundation-models.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
