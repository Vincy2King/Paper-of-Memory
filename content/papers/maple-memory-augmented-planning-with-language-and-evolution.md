# MAPLE: Memory-Augmented Planning with Language and Evolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.11636v1
- Published: 2026-09-10
- Updated: 2026-09-10
- Authors: Kesheng Chen, Yamin Hu, Wenjian Luo
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.11636v1

## One-Sentence Summary
Domain practitioners understand their business constraints but may lack operations-research expertise or dedicated support.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Domain practitioners understand their business constraints but may lack operations-research expertise or dedicated support.

进一步看，论文的核心做法或实验重点可以概括为：LLM-based optimization agents translate natural-language requirements into models or solver programs that established optimization tools can execute.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Domain practitioners understand their business constraints but may lack operations-research expertise or dedicated support. LLM-based optimization agents translate natural-language requirements into models or solver programs that established optimization tools can execute. This progress makes optimization more accessible, but real-world operations are dynamic: changing demand, resources, and priorities require updates to data, constraints, and objectives. Methods centered on isolated requests offer limited support for rapid adaptation that preserves earlier decisions and reuses useful search results. We introduce MAPLE (Memory-Augmented Planning with Language and Evolution), an agent for maintaining optimization problems through successive natural-language requests. MAPLE combines language-based problem construction with mathematical programming and evolutionary search. It retains the optimization program, accepted plans, earlier updates, and candidate solutions for subsequent requests. We introduce NLDO, a benchmark of 15 trajectories and 180 updates spanning selection, scheduling, rostering, routing, and cloud-resource placement. In the main evaluation, MAPLE completes all trajectories and achieves online scalar quality of 0.951 and a Pareto hypervolume ratio of 0.875. Controlled comparisons further show that maintaining executable state improves update validity and can preserve useful search information across substantial revisions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
