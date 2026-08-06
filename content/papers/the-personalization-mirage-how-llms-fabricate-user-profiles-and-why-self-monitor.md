# The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.04570v1
- Published: 2026-08-05
- Updated: 2026-08-05
- Authors: Yushi Sun, Yanjie Zhang, Rui Sheng
- Tags: persistent memory
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.04570v1

## One-Sentence Summary
Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined.

进一步看，论文的核心做法或实验重点可以概括为：We study over-inference (OI): the phenomenon where LLMs fabricate user attributes beyond what evidence supports.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined. We study over-inference (OI): the phenomenon where LLMs fabricate user attributes beyond what evidence supports. We introduce MirageBench, comprising 150 personas balanced across stereotypical, counter-stereotypical, and neutral profiles, 6 personalization tasks spanning an ``imagination gradient'', a four-way faithfulness taxonomy operationalized by an independent judge (validated against a blind human annotator on 400 claims: Cohen's kappa = 0.863 four-class, kappa = 0.900 binary), and a leaderboard of 12 models across 7 families on 143616 judged claims. We find that over-inference is pervasive: every one of the 12 models over-infers 35%--49% of its claims (cross-model mean 41.6%; claim-weighted 41.8%), with no model in this evaluation escaping it. Most strikingly, we surface a Self-Monitoring Inversion: at the model-selection level, models' self-assessed OI is negatively rank-correlated with their judge-measured OI (rho = -0.60, p = 0.044; exploratory, wide bootstrap CI [-0.90, +0.06], n = 12). The models that report the least over-inference tend to be flagged as fabricating the most, so self-reported confidence is a misleading signal for comparing models, even though within a single model self-audit still ranks that model's own claims moderately well (AUROC 0.58--0.83). We further show that OI is task-dependent (27%--59%) and that, in a multi-turn pilot, inferred attributes accumulate approximately linearly with little revision. MirageBench positions external verification, rather than model self-report, as a more reliable foundation for trustworthy personalization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
