# ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.01111v1
- Published: 2026-09-01
- Updated: 2026-09-01
- Authors: Huimin Wang, Zhengyi Zhao, Yutian Zhao
- Tags: agent, compression, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.01111v1

## One-Sentence Summary
Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines, LLM summaries, agentic memory---preserve...

进一步看，论文的核心做法或实验重点可以概括为：We introduce ClinTraceBench: 385 MIMIC-IV-derived verified dialogues with event-ID provenance, a nine-task taxonomy (T1--T9), and L0--L4 deterministic + L5 human-audit validation (98.92\% agreement).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines, LLM summaries, agentic memory---preserve the longitudinal signal clinical reasoning needs has not been measured. We introduce ClinTraceBench: 385 MIMIC-IV-derived verified dialogues with event-ID provenance, a nine-task taxonomy (T1--T9), and L0--L4 deterministic + L5 human-audit validation (98.92\% agreement). We evaluate eight history representation strategies---a no-context floor, \textit{last-visit-only}, \textit{full-context}, BGE-M3 \textit{dense-retrieval}, two compression schemes, and two agentic-memory systems (\textit{Mem0}, \textit{A-Mem})---across four backbones (DeepSeek-V3, GPT-4o-mini, Haiku~4.5, Sonnet~4.6) on 6{,}271 questions: 32 cells, 200{,}672 predictions. Four findings: (SP4) a controlled T3 injection probe isolates compression-induced \textit{relation} loss---with the attribution sentence present \textit{before} construction, \textit{Mem0}, \textit{A-Mem} and \textit{llm-summary} still recover only 0--5.3\% of the injected positives; (SP1) compressed strategies pay an aggregation tax on multi-visit trends and cross-patient comparisons; (SP2) the blind-to-full gap spans $+29.8$~pp (GPT-4o-mini) to $+62.7$~pp (Haiku); (SP3) abstention scales non-monotonically with context length. On the Pareto frontier Haiku dominates Sonnet under \textit{full-context} (\$25.76 vs.\ \$106.21), inverting the ``biggest backbone wins'' heuristic.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
