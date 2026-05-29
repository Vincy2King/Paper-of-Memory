# HARP: Measuring Harm Amplification in Multi-Agent LLM Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.27489v1
- Published: 2026-05-26
- Updated: 2026-05-26
- Authors: Md Hafizur Rahman, Zafaryab Haider, Tanzim Mahfuz, Prabuddha Chakraborty
- Tags: agent, context
- Categories: cs.CR, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.27489v1

## One-Sentence Summary
Multi-agent LLM systems decompose workflows across agents, tools, shared context, memory, and decision gates.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent LLM systems decompose workflows across agents, tools, shared context, memory, and decision gates.

进一步看，论文的核心做法或实验重点可以概括为：This modularity improves interpretability, but creates a propagation risk: a bounded perturbation to one component can be reused by other agents and amplified into system-level harm.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：context memory
- 来源分类信息：cs.CR, cs.AI, cs.LG

## Abstract Snapshot
Multi-agent LLM systems decompose workflows across agents, tools, shared context, memory, and decision gates. This modularity improves interpretability, but creates a propagation risk: a bounded perturbation to one component can be reused by other agents and amplified into system-level harm. We introduce HARP (Harm Amplification through Role Perturbation), a trace-first methodology for studying local-to-global harm amplification in multi-agent LLM systems. HARP compares paired clean and perturbed executions and records specialist outputs, tool calls, memory reads/writes, guard events, oracle logs, latency, token cost, and decisions. We define local harm as deviation from targeted agents or corrupted channels, global harm as deviation over the full trace, and harm amplification as (H_global/H_local). This complements attack success rate with a measure of how strongly orchestration spreads harm beyond the attack point. We instantiate HARP in a finance-oriented seven-agent system with a deterministic decision gate and configurable attack harness for specialist compromise, collusion, shared-context corruption, and temporal or memory-persistent attacks. Across five defenses, prompt-only defenses preserve benign utility but leave high success and stealth; pre-tool and step-level guards reduce some failures with utility or latency costs; and IntegrityGuard, a trace-consistency defense, achieves the lowest attack success and global harm but introduces utility/cost trade-offs. Results show that single-specialist compromise produces the strongest amplification, shared-context corruption yields the highest attack success, and temporal persistence produces the largest malicious impact. HARP argues that secure multi-agent evaluation must measure not only bypass, but propagation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
