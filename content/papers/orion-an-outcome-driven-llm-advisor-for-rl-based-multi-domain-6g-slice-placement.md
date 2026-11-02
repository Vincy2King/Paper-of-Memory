# ORION: An Outcome-Driven LLM Advisor for RL-Based Multi-Domain 6G Slice Placement

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.41563v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Mahmoud S. Mayaleh, Fetia Bannour, Nour-El-Houda Yellas
- Tags: agent, episodic
- Categories: cs.LG, cs.AI, cs.MA, cs.NI
- URL: http://arxiv.org/abs/2610.41563v1

## One-Sentence Summary
Deploying 6G network slices across administrative domains requires an online decision for each arriving request: which domain hosts each virtual network function, how traffic...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deploying 6G network slices across administrative domains requires an online decision for each arriving request: which domain hosts each virtual network function, how traffic crosses domain boundaries, and whether the...

进一步看，论文的核心做法或实验重点可以概括为：This joint decision problem is NP-hard under continuous arrivals.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG, cs.AI, cs.MA, cs.NI

## Abstract Snapshot
Deploying 6G network slices across administrative domains requires an online decision for each arriving request: which domain hosts each virtual network function, how traffic crosses domain boundaries, and whether the slice is admitted. This joint decision problem is NP-hard under continuous arrivals. Experiments on a parametrized family of multi-domain topologies show that no fixed planning strategy dominates across all regimes: the performance ranking reverses between topology classes, and feasible placements exist for most rejected requests but remain undiscovered. These findings identify the plan layer as the decisive performance lever. We introduce ORION, a hierarchical orchestrator in which two LLM agents translate service intents into structured requests and generate abstract placement plans. A cooperative multi-agent RL coordinator selects the cross-domain partition, treating the plan as a persistent soft prior, while per-domain agents place the functions. ORION main contribution lies at the plan layer: an outcome-driven episodic memory that records, for each completed attempt, the network-condition profile, the proposed plan, and its verified feasibility outcome. The memory feeds verified successes and labelled failures back to the planner, thereby closing the adaptation loop using deployment feasibility rather than a scalar reward assigned to the planner's own proposals. To isolate the effect of the plan quality, we evaluate the planner on held-out topology families while keeping the downstream selection and execution mechanisms fixed. Under this controlled setting, the proposed memory improves admission by $4.6$--$11.5$ percentage points over the same planner without memory, while importance-based retention accounts for most of the improvement over a first-in-first-out store.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
