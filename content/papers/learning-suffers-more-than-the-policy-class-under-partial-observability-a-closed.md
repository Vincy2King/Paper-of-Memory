# Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07228v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Idil Gözel
- Tags: agent
- Categories: cs.LG, math.OC
- URL: http://arxiv.org/abs/2608.07228v1

## One-Sentence Summary
When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one.

进一步看，论文的核心做法或实验重点可以概括为：We show that in a solvable case the bigger problem lies elsewhere.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, math.OC

## Abstract Snapshot
When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse. We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At our default setting the best policy the agent can represent is already close to optimal, costing 10.4% more than the ideal controller that observes everything. Learning does not find it. The algorithm instead comes to rest at a policy that is 35% worse than the best one available to it, and we can say exactly where and why. The cause is a bias in what the critic learns rather than a limit on what the actor can express. Because the agent cannot attribute what it sees to the part of the state it cannot observe, the critic misreads that unexplained variation as sharp curvature in its own value estimates, and the actor follows that error away from the optimum. We derive closed-form expressions for the resulting policy, for its cost, and for the one design choice that removes the problem, which is how far the learner looks ahead before trusting its own value estimates. Deep reinforcement learning experiments follow these predictions closely. Notably, giving the agent memory of past observations does not help, while changing how far it looks ahead does.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
