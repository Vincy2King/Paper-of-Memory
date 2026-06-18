# CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.18406v1
- Published: 2026-06-16
- Updated: 2026-06-16
- Authors: Jiaqi Chen, Yongqin Zeng, Shaoshen Chen, Yijian Zhang, Hai-Tao Zheng, Chunxia Ma, XiuTeng Zhou
- Tags: agent, benchmark, compression, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.18406v1

## One-Sentence Summary
Personalized dialogue agents require continuous long-term memory to maintain coherent interactions across multiple sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized dialogue agents require continuous long-term memory to maintain coherent interactions across multiple sessions.

进一步看，论文的核心做法或实验重点可以概括为：However, deploying these capabilities on consumer-grade hardware (e.g., 8 GB VRAM edge devices) introduces severe memory and compute bottlenecks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Personalized dialogue agents require continuous long-term memory to maintain coherent interactions across multiple sessions. However, deploying these capabilities on consumer-grade hardware (e.g., 8 GB VRAM edge devices) introduces severe memory and compute bottlenecks. Existing systems typically rely on isotropic cosine similarity for retrieval and heuristic rules for context compression. These approaches lack a unified theoretical foundation, frequently suffering from the hubness problem in high-dimensional retrieval and syntactic fragmentation during compression. To overcome these limitations, we propose CoreMem, a resource-efficient edge-cloud memory architecture fundamentally unified by information geometry. First, Riemannian retrieval replaces cosine matching with a locally adaptive Fisher-Rao metric, effectively penalizing hub memories via Mahalanobis distance with O(Ndr) Woodbury acceleration for real-time search. Second, Fisher-guided discrete token distillation (FDTD) introduces a hierarchical sentence-to-token compression mechanism. It derives sensitivity scores from Fisher information traces, providing a principled compression-KL tradeoff augmented with explicit structural syntax protection. Evaluated on the LOCOMO and LongMemEval-S benchmarks, CoreMem achieves strong accuracy improvements, yielding substantial gains in Open-domain (+4.51 pp) and Temporal (+4.17 pp) reasoning. Extensive profiling confirms that CoreMem operates seamlessly within a strict 8 GB VRAM budget, successfully bridging the gap between resource-constrained edge devices and the demand for theoretically grounded, lifelong memory agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
