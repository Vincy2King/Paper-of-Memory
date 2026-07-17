# MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.14252v1
- Published: 2026-07-15
- Updated: 2026-07-15
- Authors: Zihao Yu, Xiu Yuan, Chongjie Zhang
- Tags: context, retrieval
- Categories: cs.RO, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.14252v1

## One-Sentence Summary
Long-horizon robot planning requires more than predicting what actions will do next; it also requires memory of the embodied experience that makes future goals interpretable.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon robot planning requires more than predicting what actions will do next; it also requires memory of the embodied experience that makes future goals interpretable.

进一步看，论文的核心做法或实验重点可以概括为：People do not plan from the present scene alone: they draw on remembered places, object-state changes, prior procedures, and regularities revealed through repeated action.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.RO, cs.AI, cs.CL

## Abstract Snapshot
Long-horizon robot planning requires more than predicting what actions will do next; it also requires memory of the embodied experience that makes future goals interpretable. People do not plan from the present scene alone: they draw on remembered places, object-state changes, prior procedures, and regularities revealed through repeated action. We formulate Embodied Action Memory (EAM) as the capability to form, maintain, and use such experience as a persistent memory state for later decisions. MEMORA realizes EAM with a formation-consolidation-retrieval lifecycle and four typed stores: Environment Memory, Entity Memory, Activity Memory, and Inferred Knowledge. Online editing maintains object identities and state histories as new observations arrive; offline consolidation abstracts repeated experience into reusable procedures and participant-specific regularities. MEMORA-Bench evaluates this lifecycle on 45 hours of EPIC-KITCHENS-100 extension video across 18 participants through memory-grounded planning, including previously unseen goals, and a complementary memory-assessment task. Across four open-weight language models, full MEMORA--combining editing, typed stores, and consolidation--achieves the strongest aggregate results among the evaluated memory conditions. It improves memory-assessment accuracy by up to 20.5 points over the strongest controlled baseline and improves out-of-distribution Robot-Grounded Plan score by up to 16.6% relative. A qualitative two-task robot deployment study further illustrates how memory-grounded language plans can interface with downstream control, while the overall results show that editable, consolidated memory can supply remembered context for robot planning. Project page: https://yuzihaowashu.github.io/MEMORA/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
