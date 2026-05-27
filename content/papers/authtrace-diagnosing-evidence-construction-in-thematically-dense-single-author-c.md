# AuthTrace: Diagnosing Evidence Construction in Thematically Dense Single-Author Corpora

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.25382v2
- Published: 2026-05-25
- Updated: 2026-05-26
- Authors: Xiaoqing Wu, Feifei Li, Haoliang Ming, Wenhui Que
- Tags: benchmark, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.25382v2

## One-Sentence Summary
Evidence construction--the stage that determines which passages reach the language model before generation begins--is evaluated paradigm by paradigm, leaving practitioners with...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Evidence construction--the stage that determines which passages reach the language model before generation begins--is evaluated paradigm by paradigm, leaving practitioners with no principled way to diagnose which...

进一步看，论文的核心做法或实验重点可以概括为：We introduce AuthTrace, a diagnostic benchmark built on thematically dense single-author corpora where near-miss distractors share style, topic, and vocabulary with the required evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Evidence construction--the stage that determines which passages reach the language model before generation begins--is evaluated paradigm by paradigm, leaving practitioners with no principled way to diagnose which organization strategy fails, where, or why. We introduce AuthTrace, a diagnostic benchmark built on thematically dense single-author corpora where near-miss distractors share style, topic, and vocabulary with the required evidence. AuthTrace provides explicit quoted evidence, exact fan-in annotation, and a unified pack-level protocol measuring evidence recall, evidence precision, and answer correctness. A fan-in gradient--the number of source documents required to support the answer--serves as the primary diagnostic axis, enabling controlled comparison across retrieval, memory, graph, and structured-evidence paradigms. Evaluating eight systems across two QA models, we find that evidence recall is the strongest observed predictor of answer correctness under the primary reader-judge pair (r = 0.96); most failures stem from missing evidence rather than answer synthesis. Fan-in further exposes paradigm-specific collapse patterns: flat retrieval degrades 2-3x faster than thematically organized evidence construction. These results show fan-in decomposition to be a reusable diagnostic lens for identifying where evidence-construction systems fail and which paradigm best serves a given workload.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
