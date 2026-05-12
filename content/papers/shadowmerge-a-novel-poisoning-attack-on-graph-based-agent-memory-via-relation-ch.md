# ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09033v1
- Published: 2026-05-09
- Updated: 2026-05-09
- Authors: Yang Luo, Zifeng Kang, Tiantian Ji, Xinran Liu, Yong Liu, Shuyu Li, Lingyun Peng
- Tags: agent, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.09033v1

## One-Sentence Summary
Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an attacker can inject a crafted relation into...

进一步看，论文的核心做法或实验重点可以概括为：Existing agent-memory poisoning attacks mainly target flat textual records and are ineffective in graph-based memory because malicious relations often fail to be extracted, merged into the target anchor neighborhood,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an attacker can inject a crafted relation into graph memory so that it is later retrieved and influences agent behavior. Existing agent-memory poisoning attacks mainly target flat textual records and are ineffective in graph-based memory because malicious relations often fail to be extracted, merged into the target anchor neighborhood, or retrieved for the victim query. We present SHADOWMERGE, a poisoning attack against graph-based agent memory that exploits relation-channel conflicts. Its key insight is that a poisoned relation can share the same query-activated anchor and canonicalized relation channel as benign evidence while carrying a conflicting value. To realize this, we design AIR, a pipeline that converts the conflict into an ordinary interaction that can be extracted, merged, and retrieved by the graph-memory system. We evaluate SHADOWMERGE on Mem0 and three public real-world datasets: PubMedQA, WebShop, and ToolEmu. SHADOWMERGE achieves 93.8% average attack success rate, improving the best baseline by 50.3 absolute points, while having negligible impact on unrelated benign tasks. Mechanism studies show that SHADOWMERGE overcomes the three key limitations of existing agent-memory poisoning attacks, and defense analysis shows that representative input-side defenses are insufficient to mitigate it. We have responsibly disclosed our findings to affected graph-memory vendors and open sourced SHADOWMERGE.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
