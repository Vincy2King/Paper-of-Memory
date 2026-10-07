# When to Remember, When to Abstain: Category-Conditioned Retention for Reliable Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07100v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Olukunle Owolabi, Pulkit Gupta, Fei Wang
- Tags: agent
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2610.07100v1

## One-Sentence Summary
Persistent agent memory is only as reliable as its retention decision: an assertion weakly supported by its source can be stored and later reused as established fact.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent agent memory is only as reliable as its retention decision: an assertion weakly supported by its source can be stored and later reused as established fact.

进一步看，论文的核心做法或实验重点可以概括为：We study whether the retention decision should be governed by a confidence bar conditioned on the semantic category of the assertion rather than by a single global threshold, retaining well-evidenced categories...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Persistent agent memory is only as reliable as its retention decision: an assertion weakly supported by its source can be stored and later reused as established fact. We study whether the retention decision should be governed by a confidence bar conditioned on the semantic category of the assertion rather than by a single global threshold, retaining well-evidenced categories liberally while abstaining more aggressively where inference is unreliable. We evaluate this in a deployed cold-start memory pipeline on 100 synthetic personas. The empirical evaluation is motivated by a sharp reliability asymmetry: across 4{,}715 candidate assertions, only 77.9\% of value and belief assertions are supported by their source, versus 96.2\% for all other categories. A global confidence threshold cannot separate these: it either admits unsupported value claims or discards well-evidenced ones. Conditioning the threshold on category resolves the tradeoff. In repeated held-out evaluation, a stricter bar on values alone reduces unsupported retentions from 6.2\% to 4.0\% (an ${\approx}36\%$ relative reduction, modest but consistent across folds) and, as corroborating evidence, preserves an estimated 13 percentage points more coverage (95\% CI 9.8--16.0) than a global threshold at comparable retention. Our results suggest that reliable retention depends on the type of assertion, not on confidence alone, and that a category-conditioned threshold can act as a simple, effective form of selective prediction at the write boundary.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
