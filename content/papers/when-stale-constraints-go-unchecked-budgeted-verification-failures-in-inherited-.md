# When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.25553v1
- Published: 2026-08-26
- Updated: 2026-08-26
- Authors: Kazuki Nakayashiki
- Tags: agent
- Categories: cs.IR, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.25553v1

## One-Sentence Summary
An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record.

进一步看，论文的核心做法或实验重点可以概括为：Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the error avoidable without spending more?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.IR, cs.AI, cs.CL

## Abstract Snapshot
An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record. Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the error avoidable without spending more? We model supersession explicitly -- historical provenance is immutable; what changes is which record is current -- and assign by design the memory's form, the world's state (source current or superseded), and the verification policy at a fixed budget of two records: the agent's own allocation, or the same budget with one slot re-assigned to the critical provenance path or to a random record. With a constraint stated, agents inspected its provenance path in about one episode in five; when that constraint had been superseded, native allocation produced stale-consistent decisions in 77.3%, 74.7% and 74.7% of episodes across a primary run, a fresh-wording replication and a held-out domain. Re-assigning one slot to the critical path raised current-record-consistent decisions by +74.0, +72.7 and +61.3 points, positive in six of six models in each of those runs, and changed nothing when the record agreed with the memory. The held-out scenario was later found to contain a temporal inconsistency; a robustness replication with one sentence corrected, deposited externally before execution, gave +73.3 points and is reported alongside the original. The intervention uses knowledge of the critical path and is not a scheduler; it identifies that the share of stale-memory error attributable to verification allocation is close to its structural ceiling. Memory systems may need freshness or supersession signals separate from relevance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
