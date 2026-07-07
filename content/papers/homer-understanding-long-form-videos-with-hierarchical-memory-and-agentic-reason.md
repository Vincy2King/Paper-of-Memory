# Homer: Understanding Long-form Videos with Hierarchical Memory and Agentic Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.02588v1
- Published: 2026-07-01
- Updated: 2026-07-01
- Authors: Yixin Ji, Fanghua Ye, Juntao Li, Bo Zhao, Zexuan Qiu, Zhaopeng Tu, Liefeng Bo, Min Zhang
- Tags: agent, retrieval
- Categories: cs.CV, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.02588v1

## One-Sentence Summary
Multimodal large language models excel on short clips but struggle on hour-long videos in an online setting, where frames are processed incrementally under limited memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal large language models excel on short clips but struggle on hour-long videos in an online setting, where frames are processed incrementally under limited memory.

进一步看，论文的核心做法或实验重点可以概括为：Existing online methods either retain compact visual representations that lack semantic structure, or build higher-level memory stores organized around temporal proximity rather than explicit causal links, leaving...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.AI, cs.CL

## Abstract Snapshot
Multimodal large language models excel on short clips but struggle on hour-long videos in an online setting, where frames are processed incrementally under limited memory. Existing online methods either retain compact visual representations that lack semantic structure, or build higher-level memory stores organized around temporal proximity rather than explicit causal links, leaving multi-hop narrative reasoning to be reconstructed by the LLM at every query. We bridge this gap with \textsc{Homer}, a Hierarchical Online Memory Exploration and Reasoning framework. \textsc{Homer}'s memory mirrors the multi-scale structure of long videos, ranging from raw perception, to recurring entities, to events connected by explicit temporal and causal relations. Its agentic reasoner then explores this memory the way humans do, locating the relevant scene, looking up details, and composing the answer through multi-round memory retrieval, with a harness that verifies and corrects each step. \textsc{Homer} outperforms the previous best agent method by $+5.5$, $+10.8$, and $+4.4$ points on M3-Bench-robot, M3-Bench-web, and Video-MME-Long, and consistently lifts three various LLM backbones, indicating a model-agnostic structural capability for grounded retrieval over long videos.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
