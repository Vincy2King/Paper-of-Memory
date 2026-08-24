# DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.20664v1
- Published: 2026-08-21
- Updated: 2026-08-21
- Authors: Sarthak Singh
- Tags: agent, benchmark
- Categories: cs.AI, cs.SE
- URL: http://arxiv.org/abs/2608.20664v1

## One-Sentence Summary
DreamBench-SWE is a multi-session benchmark for software-agent memory hygiene in which later software tasks depend on non-inferable evidence from earlier sessions and are scored...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：DreamBench-SWE is a multi-session benchmark for software-agent memory hygiene in which later software tasks depend on non-inferable evidence from earlier sessions and are scored by executable hidden oracles.

进一步看，论文的核心做法或实验重点可以概括为：We report the original scaled v2 fold and a separately preregistered v2.1 successor audit designed after that study but frozen before successor outcome inspection.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.SE

## Abstract Snapshot
DreamBench-SWE is a multi-session benchmark for software-agent memory hygiene in which later software tasks depend on non-inferable evidence from earlier sessions and are scored by executable hidden oracles. We report the original scaled v2 fold and a separately preregistered v2.1 successor audit designed after that study but frozen before successor outcome inspection. The successor run completed 360/360 work units and 720/720 S3 cells across four conditions. In the original fold, the primary DF-hybrid--B5 contrast was null (95/180 versus 89/180; clustered p=.518, Holm p=1), not evidence of equivalence, and C9/C10 retained B0-headroom limitations. In the successor, no external memory achieved 21/180 passes (rate 0.1167), deterministic verbatim event memory 82/180 (rate 0.4556), the typed-plus-raw reference probe 83/180 (rate 0.4611), and one pinned hosted Mem0 literal-storage configuration 97/180 (rate 0.5389). The registered six-slot Family A retained unavailable slots at p=1; all three available comparisons against no memory rejected after Holm correction. Both preregistered mechanism contrasts were unavailable after pre-evaluation conformance rejection. The secondary literal-storage-versus-verbatim comparison was nonconfirmatory and sensitivity-dependent, while the comparison with the reference probe did not reject. The audit therefore supports DreamBench-SWE as a discriminating executable profile benchmark and characterizes one exact hosted-memory configuration, but it does not establish an external-system mechanism, superiority among memory-bearing conditions, equivalence, or broad product generality. The original v2.0.5 findings and artifacts remain unchanged.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
