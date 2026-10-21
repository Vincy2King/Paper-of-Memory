# Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.28315v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Masahiro Kaneko, Hiromi Arai, Timothy Baldwin
- Tags: agent
- Categories: cs.CR, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2610.28315v1

## One-Sentence Summary
Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed.

进一步看，论文的核心做法或实验重点可以概括为：We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.CL, cs.LG

## Abstract Snapshot
Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated record. Across four support models, memory raises response quality but also empirical leakage, the share of attribute values correctly inferred from the record, by a margin that widens over sessions. The cause is a loop in ordinary, non-adversarial assistance. Memory-conditioned responses carry earlier values forward, often as presuppositions, and users affirm them or leave them uncorrected, so that cues and the agent's own guesses become recorded values. The loop reinforces itself, and removing the agent's mentions of an attribute lowers its later disclosure about twice as much as single-turn effects predict. Users cannot leave it on their own, since correcting a value discloses the attribute, declining to discuss it shifts later predictions toward sensitive values, and incorrect values left in place become entrenched. The loop is best weakened at the agent's response. Instructing the agent not to state or presuppose attributes brings leakage to about the no-memory level while keeping most of the quality gains, whereas filtering or anonymizing what users say or what is stored gives up much of them.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
