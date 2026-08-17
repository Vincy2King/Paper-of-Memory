# Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.13867v1
- Published: 2026-08-14
- Updated: 2026-08-14
- Authors: Stephanie Jarmak
- Tags: agent, benchmark, retrieval
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2608.13867v1

## One-Sentence Summary
AI coding agents are commonly evaluated as models but deployed as systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI coding agents are commonly evaluated as models but deployed as systems.

进一步看，论文的核心做法或实验重点可以概括为：Their reliability depends not only on model capability, but on the harness, execution state, retrieval, memory and state management, permissions, review interfaces, and resource allocation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
AI coding agents are commonly evaluated as models but deployed as systems. Their reliability depends not only on model capability, but on the harness, execution state, retrieval, memory and state management, permissions, review interfaces, and resource allocation. This monograph examines those boundaries and develops a framework for evaluating and operating coding agents reliably. It synthesizes 164 scholarly works, 100 practitioner records, 29 benchmark records, and 17 author-system case records through a structured multivocal review, targeted update audits, software-engineering coverage analysis, and distributed-systems evidence synthesis. Across this evidence, many apparent model failures originate elsewhere in the system, while improvements at one layer often fail to propagate to end-to-end outcomes. Evaluation and operation are treated as a dependency chain in which weaknesses in task construction, execution environments, retrieval, state management, verification, or observability can invalidate downstream conclusions. The monograph contributes a versioned catalog of 206 reliability records: 193 gated practices, including 56 developed in depth, plus 13 research leads; an evidence ledger; a framework for dependency and repair asymmetry across the agent lifecycle; measurements and failure cases from operated agent systems; runnable evaluation and reliability protocols; and five reusable agent skills with evidence maps. Together, these provide a system-level methodology for distinguishing model capability from infrastructure effects, designing defensible evaluations, and building systems that recover safely when components fail. The review is structured rather than exhaustive, evidence strength varies by topic, and results depend on workload and configuration. The methods record which search lanes were executed, which remain unexecuted, and limits on evidence-grading claims.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
