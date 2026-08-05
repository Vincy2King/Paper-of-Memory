# OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery

- Source: arXiv
- Venue: N/A
- Paper ID: 2602.13769v3
- Published: 2026-02-14
- Updated: 2026-08-04
- Authors: Qi Liu, Ruochen Hao, Can Li, Wanjing Ma
- Tags: agent, compression, long-term
- Categories: cs.AI, cs.CE, cs.NE
- URL: http://arxiv.org/abs/2602.13769v3

## One-Sentence Summary
Automating heuristic design in complex, experiment-driven domains requires more than iterative mutation of solution algorithms.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automating heuristic design in complex, experiment-driven domains requires more than iterative mutation of solution algorithms.

进一步看，论文的核心做法或实验重点可以概括为：Current LLM-based evolutionary methods often rely on stochastic mutation loops that lack long-term strategic planning and a formal mechanism to learn from historical failures, leading to inefficient exploration and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, long-term
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI, cs.CE, cs.NE

## Abstract Snapshot
Automating heuristic design in complex, experiment-driven domains requires more than iterative mutation of solution algorithms. Current LLM-based evolutionary methods often rely on stochastic mutation loops that lack long-term strategic planning and a formal mechanism to learn from historical failures, leading to inefficient exploration and redundant trials. To address this, we present OR-Agent, a multi-agent research framework designed for automated heuristic design in optimization problems with rich experimental environments. OR-Agent organizes heuristic search as tree-based workflow that explicitly models branching hypothesis generation and systematic backtracking. Furthermore, to address the lack of adaptive learning in current agents, we introduce a hierarchical, optimization-inspired reflection system in which short-term reflections act as verbal gradients, long-term reflections as verbal momentum, and memory compression as semantic weight decay - collectively forming a principled mechanism for governing research dynamics. Extensive experiments on classical combinatorial optimization problems (e.g., TSP, CVRP, bin packing) and simulation-based cooperative driving scenarios demonstrate that OR-Agent outperforms strong evolutionary search baselines. All code and experimental data are publicly available at https://github.com/qiliuchn/OR-Agent.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
