# MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.26154v1
- Published: 2026-05-24
- Updated: 2026-05-24
- Authors: Xuanye Zhang, Yongsen Zheng, Zhuqin Xu, Kaiyu Zhou, Bowen Shen, Haoran Ou, Tianwei Zhang, Kwok-Yan Lam
- Tags: agent, benchmark, context, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.26154v1

## One-Sentence Summary
LLM-driven agents are capable of selecting external tools to complete users' tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-driven agents are capable of selecting external tools to complete users' tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, attackers could compromise such process, steering agents toward inappropriate/wrong tools and enabling malicious actions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
LLM-driven agents are capable of selecting external tools to complete users' tasks. However, attackers could compromise such process, steering agents toward inappropriate/wrong tools and enabling malicious actions. Most existing attacks primarily manipulate the tool metadata, which is easily detectable by auditing and may lose effectiveness as modern agents increasingly adopt memory modules to refine tool selection policies through accumulated experience. This paper proposes MemMorph, the first attack that bias tool selection by poisoning the agent's long-term memory. Rather than explicitly dictating the tool invocation decision, MemMorph injects a small number of crafted records that are disguised as technical facts, incident reports, and operational policies. These poisoned records reshape the agent's contextual perception and decision-making process, leading it to autonomously infer and select the tool preferred by the attacker. Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. Our findings expose long-term memory as a critical and under-explored attack surface in tool-augmented agents, urging the development of memory-level integrity safeguards.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
