# MemForm: Benchmarking Memory Formation Poisoning in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.14431v1
- Published: 2026-10-10
- Updated: 2026-10-10
- Authors: Haowen Pan, Pengyang Shao, Yunshan Ma, Yanzheng Jin, Naixin Zhai, Xiang Wang, Xun Yang
- Tags: agent, benchmark, context, long-term
- Categories: cs.CR, cs.CL
- URL: http://arxiv.org/abs/2610.14431v1

## One-Sentence Summary
Long-term memory enables LLM agents to learn from past interactions but exposes memory formation to adversarial influence.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables LLM agents to learn from past interactions but exposes memory formation to adversarial influence.

进一步看，论文的核心做法或实验重点可以概括为：Existing studies primarily organize memory poisoning by attack channels, corruption patterns, or lifecycle stages, leaving formation interfaces insufficiently characterized.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：agent memory, long-term memory, persistent memory
- 来源分类信息：cs.CR, cs.CL

## Abstract Snapshot
Long-term memory enables LLM agents to learn from past interactions but exposes memory formation to adversarial influence. Existing studies primarily organize memory poisoning by attack channels, corruption patterns, or lifecycle stages, leaving formation interfaces insufficiently characterized. We formulate Memory Formation Poisoning as adversarial manipulation of the interfaces through which persistent agent memory is produced and committed, and introduce MemForm, a controlled diagnostic benchmark covering five interfaces: Content, Evidence, Scope, Selection, and Path Poisoning. We introduce Selection and Path Poisoning as controlled intervention categories that isolate retention and consolidation order effects, respectively. Each category pairs clean and poisoned conditions with interface-specific controls. Evaluations across six LLMs and two response formats reveal broad susceptibility at all five interfaces under the evaluated memory protocols and implementations. Crucially, authentic experiences with successful outcomes do not guarantee reliable behavior after memory formation: changes to contextual support, retention, or consolidation order can induce undesirable downstream behavior. In particular, consolidation order can alter behavior even with identical retained experiences, depending on the memory formation procedure. Additional analyses show that interface applicability depends on memory architecture and that Path Poisoning susceptibility depends on the updater. The evaluated defenses provide incomplete mitigation that varies by interface. These findings motivate protecting both what is committed to persistent memory and how memory is formed from experiences. Code and data are available at https://github.com/opanhw/memform-code.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
