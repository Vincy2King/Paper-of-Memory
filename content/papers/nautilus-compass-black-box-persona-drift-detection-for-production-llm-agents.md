# Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09863v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Chunxiao Wang
- Tags: agent, conversation, retrieval
- Categories: cs.CR, cs.AI, cs.CL, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2605.09863v1

## One-Sentence Summary
Production LLM coding agents drift over long sessions: they forget user-specified constraints, slip into mistakes the user already flagged, and confabulate prior agreements.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Production LLM coding agents drift over long sessions: they forget user-specified constraints, slip into mistakes the user already flagged, and confabulate prior agreements.

进一步看，论文的核心做法或实验重点可以概括为：White-box approaches such as persona vectors require model weights and so cannot be applied to closed APIs (Claude, GPT-4) that most users actually interact with.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Production LLM coding agents drift over long sessions: they forget user-specified constraints, slip into mistakes the user already flagged, and confabulate prior agreements. White-box approaches such as persona vectors require model weights and so cannot be applied to closed APIs (Claude, GPT-4) that most users actually interact with. We present Nautilus Compass, a black-box persona drift detector and agent memory layer for production coding agents. The method operates entirely at the prompt-text layer: cosine similarity between user prompts and behavioral anchor texts, aggregated by a weighted top-k mean using BGE-m3 embeddings. Compass is, to our knowledge, the only public agent memory layer (among Mem0, Letta, Cognee, Zep, MemOS, smrti verified May 2026) that does not call an LLM at index time to extract facts or build a graph; raw conversation text is embedded directly. The system ships as a Claude Code plugin, an MCP 2024-11-05 A2A server (Cursor, Cline, Hermes), a CLI, and a REST API on one daemon, with a Merkle-chained audit log for tamper-evident anchor updates. On a held-out test set built from real Claude Code session traces and labeled by an independent LLM judge, Compass reaches ROC AUC 0.83 for drift detection. The embedded retrieval pipeline scores 56.6% on LongMemEval-S v0.8 and 44.4% on EverMemBench-Dynamic (n=500), topping the four published EverMemBench Table 4 baselines. LongMemEval-S 56.6% is ~30 points below recent white-box leaders (90+%); we treat that as the architectural ceiling of the no-extraction design. End-to-end reproduction cost is $3.50 (~14x cheaper than GPT-4o-judged stacks). A paired cross-vendor behavior A/B accompanies these numbers as preliminary system-level evidence. Code, anchors, frozen test data, and audit-log tooling are MIT-licensed at github.com/chunxiaoxx/nautilus-compass.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
