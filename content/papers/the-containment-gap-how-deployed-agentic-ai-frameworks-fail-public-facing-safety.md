# The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12797v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Md Jafrin Hossain, Mohammad Arif Hossain, Weiqi Liu, Nirwan Ansari
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.12797v1

## One-Sentence Summary
Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains, including government services,...

进一步看，论文的核心做法或实验重点可以概括为：We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains, including government services, healthcare triage, and financial advising. We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees. Applying six containment principles derived from a compositional model of agentic architectures, we audit three dominant frameworks (LangChain, AutoGPT, and OpenAI Agents SDK) and find no native compliance in any of them. Memory integrity, a defense against one of the most prevalent vulnerability classes, is not observed in any of the three evaluated frameworks. We validate these findings empirically: in a simulated government benefits agent built on LangChain, a single memory-poisoning write induces persistent targeted corruption across all tested seeds and backends, increasing the wrongful denial rate for targeted applicants to 88.9%. Under a complex five-factor policy, the same attack preserves aggregate accuracy while increasing targeted wrongful denials by 3.5x, rendering the corruption difficult to detect through standard monitoring. We then introduce two lightweight containment mechanisms: a memory integrity validator and a policy gate, which eliminate both attack vectors with sub-millisecond overhead (<0.2ms per call). We conclude that the current agentic framework ecosystem may not yet meet secure-by-default expectations for public-facing deployments and outline priority architectural interventions to enable trustworthy deployment in high-stakes, socially impactful applications.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
