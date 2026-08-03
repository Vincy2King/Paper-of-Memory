# Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.29167v1
- Published: 2026-07-31
- Updated: 2026-07-31
- Authors: Jinghan Xu, Yiyong Xiao, Wanru Shao, Hankai Liu, Xinjin Li
- Tags: agent, context, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2607.29167v1

## One-Sentence Summary
Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context.

进一步看，论文的核心做法或实验重点可以概括为：We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context. We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the low-trust source that should limit its authority. Existing prompt filters, content sanitizers, and tool guards do not enforce source-authority non-amplification after lossy memory consolidation. We formalize this boundary and instantiate it as Provenance-Preserving Memory Fire wall (PPMF), a lightweight memory middleware that preserves platform-maintained provenance and authorizes tool calls by matching action risk to the authority of action-relevant memories. In our schema-grounded evaluation with fixed risk policies, vulnerable consolidated memories reach up to 1.000 attack success rate(ASR); with intact platform-maintained provenance, confirmation, and risk labels, no evaluated unauthorized high-risk action passes the PPMF gate while confirmed benign actions and targeted low-risk memory use remain executable.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
