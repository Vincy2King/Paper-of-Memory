# A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.23338v2
- Published: 2026-04-25
- Updated: 2026-05-06
- Authors: Kexin Chu
- Tags: agent, benchmark
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2604.23338v2

## One-Sentence Summary
Agentic AI systems introduce a security surface that is qualitatively different from that of stateless LLMs.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic AI systems introduce a security surface that is qualitatively different from that of stateless LLMs.

进一步看，论文的核心做法或实验重点可以概括为：They persist memory, invoke external tools, coordinate with peer agents, and operate across sessions, allowing attacks to emerge not only at the prompt interface but also through architectural state, delegated...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
Agentic AI systems introduce a security surface that is qualitatively different from that of stateless LLMs. They persist memory, invoke external tools, coordinate with peer agents, and operate across sessions, allowing attacks to emerge not only at the prompt interface but also through architectural state, delegated authority, and long-horizon interactions. Existing security taxonomies, however, primarily organize threats by attack type, such as prompt injection or jailbreaking, and therefore obscure where in the agentic stack a threat arises and over what timescale it manifests. We propose the Layered Attack Surface Model (\lasm), a structural taxonomy for agentic AI security. \lasm decomposes the agentic stack into seven layers -- Foundation, Cognitive, Memory, Tool Execution, Multi-Agent Coordination, Ecosystem, and Governance -- and augments them with a four-class temporality axis covering instantaneous, session-persistent, cross-session cumulative, and sub-session-stack threats. We use this 7$\times$4 framework to analyze 116 papers from 2021--2026. The resulting map reveals that the upper layers of the agentic stack remain sharply under-explored, especially for long-horizon and stack-propagating threats; multiple documented attack regions have no corresponding defenses; and current benchmarks provide no coverage for cross-session or sub-session-stack failure modes. We further derive a cross-layer defense taxonomy, defense recipes for canonical attack classes, and a dependency DAG that separates near-term engineering gaps from fundamental research challenges. We release the per-paper coding, robustness scripts, and a reference Agent Bill of Materials schema to support reproducible analysis.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
