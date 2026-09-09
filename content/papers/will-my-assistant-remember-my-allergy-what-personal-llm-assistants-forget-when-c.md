# Will My Assistant Remember My Allergy? What Personal LLM Assistants Forget When Conversation Memory Is Compressed

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.05767v1
- Published: 2026-09-04
- Updated: 2026-09-04
- Authors: Lichen Zhu, Yueqian Lin, Yiheng Wang, Yudong Liu, Hai "Helen" Li, Yiran Chen
- Tags: agent, benchmark, compression, conversation, episodic
- Categories: cs.HC
- URL: http://arxiv.org/abs/2609.05767v1

## One-Sentence Summary
Personal LLM assistants (health companions, elder-care agents, accessibility aides) are judged by what they remember about a person: a medication or an allergy mentioned in...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal LLM assistants (health companions, elder-care agents, accessibility aides) are judged by what they remember about a person: a medication or an allergy mentioned in passing and needed days later.

进一步看，论文的核心做法或实验重点可以概括为：Privacy pushes them on-device, where a month of conversation can outgrow the model's own weights, so an eviction policy must decide what the cache forgets.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, conversation, episodic
- 检索关键词命中：conversational memory
- 来源分类信息：cs.HC

## Abstract Snapshot
Personal LLM assistants (health companions, elder-care agents, accessibility aides) are judged by what they remember about a person: a medication or an allergy mentioned in passing and needed days later. Privacy pushes them on-device, where a month of conversation can outgrow the model's own weights, so an eviction policy must decide what the cache forgets. Benchmarks report that eviction keeps such facts at a 20% budget, but they compress a prompt that already contains the user's future question, foresight no cache-reusing assistant has. Hide the question until after compression and the advantage vanishes: on PA-Bench, 100 assistant conversations we construct, an allergy mentioned in passing survives to the question that needs it 0--1% of the time, against 97% with full memory. The cause is the budget, not the scorer: none of the training-free policies we evaluate ranks the fact high enough, and the budget that would keep it is too large to bother compressing. A compressed cache is an inference-reuse mechanism, not a persistence layer: safety-critical facts need an auditable episodic store alongside it, and an interface that asks rather than invents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
