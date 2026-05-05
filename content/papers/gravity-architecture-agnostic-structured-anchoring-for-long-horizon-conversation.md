# GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.01688v1
- Published: 2026-05-03
- Updated: 2026-05-03
- Authors: Yushi Sun, Bowen Cao, Dong Fang, Lingfeng Su, Wai Lam
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.01688v1

## One-Sentence Summary
Long-horizon conversational agents rely on memory systems with increasingly sophisticated retrieval mechanisms.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon conversational agents rely on memory systems with increasingly sophisticated retrieval mechanisms.

进一步看，论文的核心做法或实验重点可以概括为：However, retrieved fragments are typically fed to the language model as unstructured text, lacking the relational, temporal, and thematic structures essential for complex reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-horizon conversational agents rely on memory systems with increasingly sophisticated retrieval mechanisms. However, retrieved fragments are typically fed to the language model as unstructured text, lacking the relational, temporal, and thematic structures essential for complex reasoning. To bridge this reasoning gap, we introduce GRAVITY (\textbf{G}eneration-time \textbf{R}elational \textbf{A}nchoring \textbf{V}ia \textbf{I}njected \textbf{T}opological Memor\textbf{Y}), a plug-and-play structured memory module. GRAVITY extracts three complementary knowledge representations from raw conversational utterances: entity profiles grounded in relational graphs, temporal event tuples linked into causal traces, and cross-session topic summaries. At generation time, it injects these representations into the host system's prompt as structured anchoring contexts. This approach effectively synthesizes scattered evidence into a coherent, query-relevant context without requiring any architectural modifications to the host model. Extensive evaluations across five diverse memory systems on the LongMemEval and LoCoMo benchmarks demonstrate the efficacy of our approach. On average, GRAVITY improves LLM-judge accuracy by 7.5--10.1%. Gains are inversely correlated with baseline strength: the weakest host improves by 12.2% while the strongest still gains 3.8--5.7%. These findings establish structured context anchoring as a broadly effective, architecture-agnostic augmentation paradigm for long-horizon conversational memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
