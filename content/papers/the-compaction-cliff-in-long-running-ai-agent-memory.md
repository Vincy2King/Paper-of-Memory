# The Compaction Cliff in Long-Running AI Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22752v1
- Published: 2026-08-24
- Updated: 2026-08-24
- Authors: Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer
- Tags: agent, benchmark, context, episodic
- Categories: cs.AI, cs.IR
- URL: http://arxiv.org/abs/2608.22752v1

## One-Sentence Summary
A safety rule and an episodic log compete for the same tokens in an AI agent's context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A safety rule and an episodic log compete for the same tokens in an AI agent's context.

进一步看，论文的核心做法或实验重点可以概括为：When the budget overflows, both are summarized at the same rate; only the rule needs exact wording to remain enforceable.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.IR

## Abstract Snapshot
A safety rule and an episodic log compete for the same tokens in an AI agent's context. When the budget overflows, both are summarized at the same rate; only the rule needs exact wording to remain enforceable. On 20 production agent configurations, Claude Code's /compact prompt on Sonnet 4.6 preserves 53\% of safety rules after one compaction round and 10\% after five. We name this the Compaction Cliff. We address it with Knowledge Triage, a framework that classifies each line of an agent's knowledge base by type and routes each type through its own retention policy. Three deterministic operators implement this triage across the three context-management operations: TypeCompact rewrites items in place under per-type fidelity, TypeDecompose partitions a topic too large to compact safely, replicating in-scope safety rules across partitions, and TypeRetrieve fetches items from external storage with in-scope rules pinned ahead of relevance. On five public corpora, TypeCompact preserves 2--4$\times$ more safety rules than the strongest single-shot LLM compactor at every ratio, with 96\% recall over five rounds. TypeDecompose reaches 0\% locality violations against 93\% under uniform partitioning. TypeRetrieve reaches 100\% recall@50 against 73\% for the best single-shot LLM retriever. On three downstream behavioral benchmarks, we outperform the production Sonnet compactor on medical compliance (paired McNemar $p < 10^{-8}$ on preservation, $N = 200$), the full-policy and hierarchical baselines on retail task pass rate ($p < 0.01$, $N = 115$), and the hierarchical compaction on the airline domain ($p = 0.024$). We release AgentArtifactCorpus (396{,}934 agent configurations from 54{,}628 public GitHub repositories), the classifier, and the reference implementation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
