# EA-Graph: Artifact-Anchored Verification Memory for Coding Agents under Upstream Drift

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.04278v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Hwai-Jung Hsu, Cheng-Jan Chi, Hanna Everett
- Tags: agent
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2608.04278v1

## One-Sentence Summary
Coding agents increasingly work across sessions, but prose notes can preserve a conclusion without the program state that supported it.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Coding agents increasingly work across sessions, but prose notes can preserve a conclusion without the program state that supported it.

进一步看，论文的核心做法或实验重点可以概括为：After an upstream change, a repository may still build even though earlier verification claims are no longer valid.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
Coding agents increasingly work across sessions, but prose notes can preserve a conclusion without the program state that supported it. After an upstream change, a repository may still build even though earlier verification claims are no longer valid. EA-Graph is an artifact-anchored memory for verification claims. It represents artifacts at sub-path granularity, resolves aliases to leaf definitions, anchors each claim to the content used to establish it, and keeps evidence strength separate from freshness. When replacement content is unavailable, the claim becomes unprovable rather than guessed. EA-Graph is evaluated on generated repositories whose behavior-to-artifact ground truth is known by construction. The task is to classify prior claims as unaffected, affected, or unprovable after value drift, logic drift, and deliberately withheld upstream content. The analysis covers 42 sessions across seven clean worlds, 14 model-world instances, three memory conditions, and two model tiers. In the Haiku round, artifact-anchored memory outscored prose notes and no persistent memory in all seven worlds; each exact paired Wilcoxon comparison yielded p = 0.0156. In the Sonnet round, the anchored condition was perfect, but frequent control ceilings left the preregistered contrasts non-significant. No session fabricated withheld content. These results support a bounded claim: artifact-anchored memory improved the smaller model's provability judgments in this testbed. An exploratory comparison further suggests that structured claim memory may narrow a capability gap by externalizing in-session re-derivation, but it does not establish cross- model equivalence. The study makes no claim about efficiency or repair quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
