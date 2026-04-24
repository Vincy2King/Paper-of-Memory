# MEMRES: A Memory-Augmented Resolver with Confidence Cascade for Agentic Python Dependency Resolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.16941v1
- Published: 2026-04-18
- Updated: 2026-04-18
- Authors: Dao Sy Duy Minh, Tran Chi Nguyen, Trung Kiet Huynh, Pham Phu Hoa, Nguyen Lam Phu Quy, Vu Nguyen
- Tags: agent
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2604.16941v1

## One-Sentence Summary
We present MEMRES, an agentic system for Python dependency resolution that introduces a multi-level confidence cascade where the LLM serves as the last resort.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present MEMRES, an agentic system for Python dependency resolution that introduces a multi-level confidence cascade where the LLM serves as the last resort.

进一步看，论文的核心做法或实验重点可以概括为：Our system combines: (1) a Self-Evolving Memory that accumulates reusable resolution patterns via tips and shortcuts; (2) an Error Pattern Knowledge Base with 200+ curated import-to-package mappings; (3) a Semantic...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
We present MEMRES, an agentic system for Python dependency resolution that introduces a multi-level confidence cascade where the LLM serves as the last resort. Our system combines: (1) a Self-Evolving Memory that accumulates reusable resolution patterns via tips and shortcuts; (2) an Error Pattern Knowledge Base with 200+ curated import-to-package mappings; (3) a Semantic Import Analyzer; and (4) a Python 2 heuristic detector resolving the largest failure category. On HG2.9K using Gemma-2 9B (10 GB VRAM). MEMRES resolves 2503 of 2890 (86.6%, 10-run average) snippets, combining intra-session memory with our confidence cascade for the remainder. This already exceeds PLLM's 54.7% overall success rate by a wide margin.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
