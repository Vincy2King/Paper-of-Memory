# The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34767v1
- Published: 2026-10-26
- Updated: 2026-10-26
- Authors: Yuexi Pan, Yongchao Chen
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.34767v1

## One-Sentence Summary
Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history?

进一步看，论文的核心做法或实验重点可以概括为：Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history? Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use. The same reported test result can support confirmation when the outcome and stopping rule were fixed in advance, yet only exploration when the outcome was selected from twenty inspected results. We call this scientific use validity: whether remembered evidence is eligible to influence a decision under the state governing its interpretation. We introduce SciValidityBench, an executable benchmark factory with 64 TaskSpecs spanning five validity modules and six scientific domains. TaskSpecs couple generated experimental histories with scientific-state definitions, programmatic decision oracles, controlled interventions, and automatic scoring. The SciStateForge compiler-reader framework turns distributed histories into explicit decision-governing state. Counterfactual pairs and targeted corruption-repair controls then test whether models use those dependencies and localize failures. Across four model families, compiled scientific state improves valid decision-making by 9.2-18.8 percentage points over a generic Event Graph. Retrieval alone does not reproduce this cross-family gain, while content-identical flat and typed views show that the improvement comes from exposing governing state rather than a particular graph serialization. SciValidityBench thus shifts memory evaluation from finding the right fact to deciding whether that fact should control the decision.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
