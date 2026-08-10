# LifelongCrossNav: Persistent 3D Semantic Memory for Cross-Floor Multi-Object Navigation

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07079v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Zehui Li, Zihao Sun, Jiawei Xu, Zheqi He, Xiaoqiang Zhang, Jing-Shu Zheng, Lu Liu, Dahui Gao, Xiuwan Chen
- Tags: agent, benchmark, retrieval
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2608.07079v1

## One-Sentence Summary
Object-goal navigation has made substantial progress in semantic perception and exploration, yet persistent memory for multi-object navigation and cross-floor navigation are...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Object-goal navigation has made substantial progress in semantic perception and exploration, yet persistent memory for multi-object navigation and cross-floor navigation are still commonly addressed separately.

进一步看，论文的核心做法或实验重点可以概括为：We present LifelongCrossNav, a framework for sequential multi-object ObjectNav in unknown multi-floor indoor environments.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Object-goal navigation has made substantial progress in semantic perception and exploration, yet persistent memory for multi-object navigation and cross-floor navigation are still commonly addressed separately. We present LifelongCrossNav, a framework for sequential multi-object ObjectNav in unknown multi-floor indoor environments. Within each episode, the agent receives an ordered sequence of object-goal queries while continuously maintaining a shared sparse 3D semantic voxel memory. This memory incrementally accumulates geometric structure, traversability states, and vision-language features, allowing subsequent object-goal queries to retrieve previously acquired scene information without rebuilding the map. To support persistent search across floors, LifelongCrossNav combines support-aware 3D traversability mapping, stair-specific perception, and direction-aware stair traversal. A unified navigation policy coordinates same-floor frontier exploration, live and historical point-of-interest retrieval, stair navigation, and target-object search and approach. We further introduce HM3D-MFMON, a benchmark for sequential Multi-Floor Multi-Object Navigation built on HM3D scenes, including a dedicated subset in which completing the full sequence of object-goal subtasks requires at least one floor transition. Experimental results show that LifelongCrossNav consistently outperforms a representative planar persistent semantic-map baseline on HM3D-MFMON, demonstrating that persistent 3D semantic memory and cross-floor traversability modeling effectively support sequential multi-object navigation in multi-floor environments. Project page: https://flageval-baai.github.io/LifelongCrossNavPage.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
