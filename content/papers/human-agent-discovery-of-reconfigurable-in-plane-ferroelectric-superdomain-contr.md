# Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.06887v1
- Published: 2026-09-07
- Updated: 2026-09-07
- Authors: Yu Liu, Boris Slautin, Ching-Che Lin, Jaegyu Kim, Lane W. Martin, Sergei V. Kalinin
- Tags: agent
- Categories: cond-mat.mtrl-sci, cs.AI
- URL: http://arxiv.org/abs/2609.06887v1

## One-Sentence Summary
Automated experimentation is most effective when the observables, available actions, and objective are defined before the experiment starts, as is the case for Bayesian...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automated experimentation is most effective when the observables, available actions, and objective are defined before the experiment starts, as is the case for Bayesian optimization.

进一步看，论文的核心做法或实验重点可以概括为：However, in many exploratory experiments, the variables that describe the sample must be extracted from the data, new operations emerge during the experiments, and the instrument budget is too small to learn the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cond-mat.mtrl-sci, cs.AI

## Abstract Snapshot
Automated experimentation is most effective when the observables, available actions, and objective are defined before the experiment starts, as is the case for Bayesian optimization. However, in many exploratory experiments, the variables that describe the sample must be extracted from the data, new operations emerge during the experiments, and the instrument budget is too small to learn the problem by trials. Here we introduce the Scanning Probe Agentic Research Cycle (SPARC) framework, in which a coding agent and a human operator share one microscope, one notebook, and two persistent memory files. FINDINGS.md stores graded conclusions about the experiment, whereas PITFALLS.md records learned failure modes of analysis and instrument. We apply SPARC to reconfigure the in-plane superdomain direction of a (111)-oriented PbZr0.2Ti0.8O3 film. In an operator-supervised campaign, the agent reanalyzed earlier manual measurements and developed an oriented lattice of stationary bias pulses with alternating polarity to reconfigure the superdomain direction. In a subsequent agent-controlled campaign, PITFALLS.md entries were compiled into checks that validate a design before any write. The experiments showed that spatial polarity alternation, instead of the exact matching between the lattice and lamellar periods, determines directional selection. Combining a raster scan with a masked pulse lattice printed the letters UTK into the superdomain orientation. The campaign also identified practical requirements for agentic experimentation where physical verification of instrument execution, the conditions under which stored findings remain valid, validation of new observables on instrument data, and robust control protocols.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
