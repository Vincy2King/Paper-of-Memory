# LatentMem: Customizing Latent Memory for Multi-Agent Systems

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:n5GFzuQpA3
- Published: 2026-12-31
- Updated: 2026-05-27
- Authors: {'fullname': 'Muxin Fu', 'username': ''}, {'fullname': 'Guibin Zhang', 'username': ''}, {'fullname': 'Xiangyuan Xue', 'username': '~Xiangyuan_Xue1'}, {'fullname': 'Yafu Li', 'username': ''}, {'fullname': 'Zefeng He', 'username': ''}, {'fullname': 'Siyuan Huang', 'username': ''}, {'fullname': 'Xiaoye Qu', 'username': ''}, {'fullname': 'Yu Cheng', 'username': ''}, {'fullname': 'Yang Yang', 'username': ''}
- Tags: agent, benchmark, context
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=n5GFzuQpA3

## One-Sentence Summary
Large language model (LLM)-powered multi-agent systems (MAS) demonstrate remarkable collective intelligence, wherein multi-agent memory serves as a pivotal mechanism for...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language model (LLM)-powered multi-agent systems (MAS) demonstrate remarkable collective intelligence, wherein multi-agent memory serves as a pivotal mechanism for continual adaptation.

进一步看，论文的核心做法或实验重点可以概括为：However, existing multi-agent memory designs remain constrained by two fundamental bottlenecks: (i) memory homogenization arising from the absence of role-aware customization, and (ii) information overload induced by...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Large language model (LLM)-powered multi-agent systems (MAS) demonstrate remarkable collective intelligence, wherein multi-agent memory serves as a pivotal mechanism for continual adaptation. However, existing multi-agent memory designs remain constrained by two fundamental bottlenecks: (i) memory homogenization arising from the absence of role-aware customization, and (ii) information overload induced by excessively fine-grained memory entries. To address these limitations, we propose LatentMem, a learnable multi-agent memory framework designed to customize agent-specific memories in a token-efficient manner. Specifically, LatentMem comprises an experience bank that stores raw interaction trajectories in a lightweight form, and a memory composer that synthesizes compact latent memories conditioned on retrieved experience and agent-specific contexts. Further, we introduce Latent Memory Policy Optimization (LMPO), which propagates task-level optimization signals through latent memories to the composer, encouraging it to produce compact and high-utility representations. Extensive experiments across diverse benchmarks and mainstream MAS frameworks show that LatentMem achieves a performance gain of up to $19.36$% over vanilla settings and consistently outperforms existing memory architectures, without requiring any modifications to the underlying frameworks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
