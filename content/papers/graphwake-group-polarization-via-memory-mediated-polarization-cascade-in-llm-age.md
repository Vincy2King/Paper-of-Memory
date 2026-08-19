# GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.17665v1
- Published: 2026-08-18
- Updated: 2026-08-18
- Authors: Haoran Bu, Zejian Chen, Litian Zhang, Xi Zhang
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.17665v1

## One-Sentence Summary
LLM-driven agents can autonomously exchange opinions on online platforms and form communities.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-driven agents can autonomously exchange opinions on online platforms and form communities.

进一步看，论文的核心做法或实验重点可以概括为：Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are difficult to realize in practice. We therefore formulate a new threat, Memory-Mediated Polarization Cascade, which uses agent memory as a persistence channel and public discussion as a propagation channel. This threat contains three stages. During exposure and memory retention, the attacker exposes a small set of target agents to arguments that reinforce their respective stated stances. The targets' memory systems then process and retain these arguments. During retrieval and reproduction, a shared stance-neutral discussion cues the targets to retrieve and reproduce their respective retained arguments. During iterative propagation, untreated agents influenced by the reproduced arguments restate and spread them. We instantiate this threat in GraphWake with three components: (i) stance-support argumentation knowledge graphs construct knowledge-based arguments; (ii) axiom-oriented triple selection distills them for reliable retention and reproduction; and (iii) stance-neutral memory cueing triggers concurrent retrieval and reproduction, initiating propagation. Experiments across multiple discussions and memory systems show that GraphWake substantially increases group polarization. These findings reveal a community-level polarization risk.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
