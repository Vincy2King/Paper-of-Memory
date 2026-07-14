# Context by Distinct Information: An Auditable Dirichlet-Process Working Memory for Long, Redundant Context Streams

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.10441v1
- Published: 2026-07-11
- Updated: 2026-07-11
- Authors: Siddharth Pal, Viktoria Rojkova
- Tags: context
- Categories: cs.LG, cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2607.10441v1

## One-Sentence Summary
Context engineering decides what information a model carries forward, and current designs meter it in tokens: compressing the past into a bounded recurrent state, keeping a key-...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Context engineering decides what information a model carries forward, and current designs meter it in tokens: compressing the past into a bounded recurrent state, keeping a key-value entry for every token, or imposing...

进一步看，论文的核心做法或实验重点可以概括为：All three make the token the unit of memory even when the stream is redundant and the task depends on the distinct information it carries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Context engineering decides what information a model carries forward, and current designs meter it in tokens: compressing the past into a bounded recurrent state, keeping a key-value entry for every token, or imposing a fixed budget through a window or eviction rule. All three make the token the unit of memory even when the stream is redundant and the task depends on the distinct information it carries. Building on a companion mechanism paper that opens a cache slot only when an incoming key is novel, so memory scales with the number of distinct items rather than tokens, we develop that allocate-on-novelty cache as a working-memory component and organize context by how a task depends on the past: recall-carried information belongs in a content-addressed novelty cache, summary-carried information in a recurrent state, and locality-carried information in a recency window. The claim is empirical and bounded. On a matched character-level control, novelty-gated attention reaches full-attention performance while attending to about half the tokens, and coupling the cache with a state-space summary matches full-attention coupling at that reduced cost; the advantage grows as context lengthens, while a sliding window is preferable on short, locality-dominated spans. On next-code prediction over synthetic Medicare claims the coupled component leads full attention and every fixed-budget eviction policy at a thousand-event horizon, whereas cost forecasting over the same stream is summary-carried and the cache is neutral. The retained memory is an inspectable table of templates, codes, drugs, or places rather than an opaque state. The experiments are small-scale and use only public data; they establish the primitive that context can scale with distinct information rather than tokens, in a working memory that is content-addressable and auditable.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
