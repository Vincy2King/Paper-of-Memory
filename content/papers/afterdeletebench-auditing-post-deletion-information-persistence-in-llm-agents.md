# AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.31366v1
- Published: 2026-10-22
- Updated: 2026-10-22
- Authors: Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian, Raef Bassily, Andrew Perrault
- Tags: agent
- Categories: cs.CR, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2610.31366v1

## One-Sentence Summary
Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries.

进一步看，论文的核心做法或实验重点可以概括为：Deleting an original memory record therefore need not remove information carried by its descendants.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.CL, cs.LG

## Abstract Snapshot
Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion recovery to be attributed to the original exposure. In our primary setting, a single query recovers the deleted secret from Qwen2.5-7B-Instruct in roughly two thirds of cases, while matched never-exposed controls have zero recovery. Crucially, recovery does not require a surviving verbatim copy: when the complete secret string is absent and only separately stored components remain under a public composition rule, exact reconstruction succeeds in 62-99% of cases across Qwen, Mistral, and Phi-3. We also show that the response interface is part of the measurement system: target-bearing replies can be scored as failures when the requested format and parser are misaligned. Finally, we separate reconstruction from write-back and fresh-session recall. Provenance-aware closure eliminates observed recovery in the tested positive-baseline settings, whereas an exact-literal write filter blocks reinsertion but cannot erase information already present. Together, these results show that source deletion should be evaluated behaviorally at the level of the agent and its memory system, not only as a storage operation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
