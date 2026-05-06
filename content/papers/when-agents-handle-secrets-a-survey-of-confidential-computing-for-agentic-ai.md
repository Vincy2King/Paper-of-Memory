# When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.03213v1
- Published: 2026-05-04
- Updated: 2026-05-04
- Authors: Javad Forough, Marios Kogias, Hamed Haddadi
- Tags: agent, context
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.03213v1

## One-Sentence Summary
Agentic AI systems, specifically LLM-driven agents that plan, invoke tools, maintain persistent memory, and delegate tasks to peer agents via protocols such as MCP and A2A,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic AI systems, specifically LLM-driven agents that plan, invoke tools, maintain persistent memory, and delegate tasks to peer agents via protocols such as MCP and A2A, introduce a threat surface that differs...

进一步看，论文的核心做法或实验重点可以概括为：Agents accumulate sensitive context, hold credentials, and operate across pipelines no single party fully controls, enabling prompt injection, context exfiltration, credential theft, and inter-agent message poisoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Agentic AI systems, specifically LLM-driven agents that plan, invoke tools, maintain persistent memory, and delegate tasks to peer agents via protocols such as MCP and A2A, introduce a threat surface that differs materially from standalone model inference. Agents accumulate sensitive context, hold credentials, and operate across pipelines no single party fully controls, enabling prompt injection, context exfiltration, credential theft, and inter-agent message poisoning. Current defenses operate entirely within the software stack and can be silently bypassed by a sufficiently privileged adversary such as a compromised cloud operator. Confidential computing (CC) offers a hardware-rooted alternative: Trusted Execution Environments (TEEs) isolate agent code and data from privileged system software, while remote attestation enables verifiable trust across distributed deployments. This survey synthesizes the design space in four parts: (i) a unified taxonomy of six TEE platforms (Intel SGX, Intel TDX, AMD SEV-SNP, ARM TrustZone, ARM CCA, and NVIDIA H100 CC) covering deployment roles and performance tradeoffs; (ii) an agent-centric threat model spanning perception, planning, memory, action, and coordination layers mapped to nine security goals; (iii) a comparative survey of CC-based defenses distinguishing findings that transfer from single-call inference versus what requires new agentic designs; and (iv) six open challenges including compound attestation for multi-hop agent chains and GPU-TEE performance at LLM scale. While several hardware trust primitives appear mature enough for targeted deployments, no broadly established end-to-end framework yet binds them into a coherent security substrate for production agentic AI.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
