# Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38021v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Christopher J. Chanhnourack
- Tags: agent, context, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2609.38021v1

## One-Sentence Summary
We evaluate an auditable long-term memory system on LongMemEval-S.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We evaluate an auditable long-term memory system on LongMemEval-S.

进一步看，论文的核心做法或实验重点可以概括为：Its retrieval chain uses hybrid candidate retrieval, cross-encoder reranking, coverage-first packet compilation, and deterministic reasoning scaffolds; an LLM is used only as a replaceable final reader.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
We evaluate an auditable long-term memory system on LongMemEval-S. Its retrieval chain uses hybrid candidate retrieval, cross-encoder reranking, coverage-first packet compilation, and deterministic reasoning scaffolds; an LLM is used only as a replaceable final reader. The chain places all gold sessions in the candidate pool for 468/470 answerable questions and produces gold-complete packets for 462/470. With a Claude Opus reader called through an unpinned CLI alias, two 500-question passes score 479/500 and 475/500 under GPT-4o. The 72 answerable knowledge-update rows used a substantively modified scoring prompt whose effect under the official text has not been measured. The pair straddles Chronos High's published 478/500; differences in reader generation, scoring prompt, and possibly data version, plus within-system variance, establish neither superiority nor equivalence. A grok-4.6-high reader on the same packets scores 476/474, while a maximum-reasoning-effort agentic variant regresses to 461/465. The headline passes differ on eight verdict-flip rows. A second judge agrees with the headline judge on 493/500 rows (98.6%) in each pass and scores both passes 472/500; the official judge also flips three verdicts when re-scoring byte-identical pass-1 answers. Negative controls rejected a verifier that repaired three wrong drafts but broke eleven correct drafts. All components were developed on the same 500 questions, with no held-out evaluation or independent human adjudication; retrieval and scaffold method sources and transcript-derived audits are held; and the headline reader received extra operator context, its complete requests were not retained, and MCP tool availability is unresolved. We release materialized packets, scaffolds, reader outputs, judge verdicts, and controls for inspection and re-scoring.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
