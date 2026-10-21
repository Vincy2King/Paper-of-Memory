# Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27230v1
- Published: 2026-10-19
- Updated: 2026-10-19
- Authors: Tao Jiang, Benjamin Navet, Yousouf Taghzouti, Fabien Gandon, Louis-Félix Nothias, Élise Dumont
- Tags: agent
- Categories: cs.AI, q-bio.BM
- URL: http://arxiv.org/abs/2610.27230v1

## One-Sentence Summary
Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available.

进一步看，论文的核心做法或实验重点可以概括为：Increasing automation within the chemical sciences leads to a more digital and precision chemistry.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, q-bio.BM

## Abstract Snapshot
Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more digital and precision chemistry. Dedicated scientific agents are becoming central to guiding the chemist through an ever-increasing amount of data and findings, including negative ones. Here, we introduce Magnolia, a persistent-memory artificial intelligence agent framework that integrates computational protocols, from docking to quantum chemistry, lab notebooks and chat logs relying on large language models (LLMs). It relies on a three-tier memory system: session-level observations are automatically captured and distilled into structured learnings, confirmed and elevated to project-tier entries and, when human-validated, promoted to cross-project rules that actively guide subsequent work and provide direct chemical feedback. We illustrate Magnolia on four case studies: quantum-chemical evaluation of aromatic systems (COMPAS database), molecular dynamics of butane and of modified DNA, and a protein-peptide docking campaign. Across these projects, Magnolia tracked 317 runs and accumulated 116 project-tier entries, from which four cross-project rules were promoted; in controlled replays of four tasks, runs with memory passed the checks that runs without it failed (for example, ten of ten docking-configuration checks, against one to four of ten). By combining automation, reproducibility, and human-in-the-loop control, our Magnolia framework streamlines docking, molecular dynamics and quantum chemistry calculations with direct analysis and LLM-augmented feedback, offering accelerated access to computational (bio)chemistry.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
