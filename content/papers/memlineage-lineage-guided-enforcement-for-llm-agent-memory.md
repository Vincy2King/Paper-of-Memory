# MemLineage: Lineage-Guided Enforcement for LLM Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.14421v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Ciyan Ouyang, Rui Hou
- Tags: agent
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.14421v1

## One-Sentence Summary
We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry.

进一步看，论文的核心做法或实验重点可以概括为：Recent and concurrent work shows that untrusted content can be written into persistent agent state and re-enter later sessions as an instruction; the remaining systems question is how to preserve useful memory recall...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry. Recent and concurrent work shows that untrusted content can be written into persistent agent state and re-enter later sessions as an instruction; the remaining systems question is how to preserve useful memory recall while preventing such state from justifying sensitive actions. MemLineage treats this as a chain-of-custody problem rather than a filtering problem. It is a six-module design around an RFC-6962 Merkle log over per-principal Ed25519-signed entries: a weighted derivation DAG records which retrieved entries influenced each new memory, and a max-of-strong-edges propagation rule makes Untrusted-Path Persistence hold for any chain whose attribution edges remain above threshold. The sensitive-action gate then refuses dispatches whose active justification descends from an external ancestor, while still allowing benign recall. We evaluate three defense cells against three memory-poisoning workloads on a deterministic mechanism-isolation harness; MemLineage is the only configuration in that harness that drives all three columns to zero ASR, while sub-millisecond per-operation overhead keeps it well below the noise floor of any LLM call. A Codex-backed AgentDojo bridge further separates strong-model behavior from defense-layer behavior: under an intentionally vulnerable tool-output profile, no-defense and signature-only baselines fail on all six banking pairs, while all MemLineage rows reduce strict AgentDojo ASR to zero. The core deterministic artifacts are byte-equal CI-verified; hosted-model AgentDojo and live-model sweeps are recorded as auditable logs rather than byte-pinned artifacts.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
