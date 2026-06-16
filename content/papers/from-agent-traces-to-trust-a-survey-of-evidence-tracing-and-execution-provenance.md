# From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04990v2
- Published: 2026-06-03
- Updated: 2026-06-14
- Authors: Yiqi Wang, Jiaqi Zhang, Taotao Cai, Zirui Liu, Qingqiang Sun, Zequn Sun, Zhangkai Wu, Manqing Dong, Mingkai Zhang, Xuefei Yin, Yanming Zhu
- Tags: agent, benchmark, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2606.04990v2

## One-Sentence Summary
Large language model (LLM)-based agents are evolving from passive text generators into autonomous systems capable of planning, tool use, retrieval, memory access, environmental...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM)-based agents are evolving from passive text generators into autonomous systems capable of planning, tool use, retrieval, memory access, environmental interaction, and multi-agent collaboration.

进一步看，论文的核心做法或实验重点可以概括为：These capabilities expand agent autonomy, but also make agent behavior harder to verify, debug, and audit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Large language model (LLM)-based agents are evolving from passive text generators into autonomous systems capable of planning, tool use, retrieval, memory access, environmental interaction, and multi-agent collaboration. These capabilities expand agent autonomy, but also make agent behavior harder to verify, debug, and audit. Final-answer accuracy alone cannot explain how an output was produced, which evidence supported each claim, whether tool calls were justified, how memory influenced later decisions, or where failures originated. This survey examines evidence tracing and execution provenance as foundations for process-level accountability in trustworthy LLM agents. We define execution provenance as the typed graph of an agent execution and evidence tracing as its projection onto evidence-support relations. This perspective connects retrieval grounding, claim support, tool-use safety, memory lineage, observability, debugging, audit, and recovery within a unified framework. We introduce a taxonomy covering trace sources, evidence and execution units, provenance relations, tracing granularity and timing, representation forms, and trust functions. We then review key methodological directions, including provenance representation, evidence attribution, tool-use provenance, runtime guardrails, provenance-bearing memory, observability, and failure diagnosis. Finally, we discuss benchmarks, datasets, metrics, and open challenges for building provenance-aware, auditable, and recoverable agent systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
