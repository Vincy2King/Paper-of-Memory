# HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.07263v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Jongwoo Ko, Pashmina Cameron
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.07263v1

## One-Sentence Summary
Parallel block drafting accelerates speculative decoding by predicting multiple future positions in a single backbone pass, but on-device deployment constrains both drafter...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Parallel block drafting accelerates speculative decoding by predicting multiple future positions in a single backbone pass, but on-device deployment constrains both drafter capacity and context storage.

进一步看，论文的核心做法或实验重点可以概括为：Under tight memory budgets, drafters must model long-range dependencies and fine-grained draft-position interactions without the growing KV-cache overhead of full-context attention.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory compression
- 来源分类信息：cs.CL

## Abstract Snapshot
Parallel block drafting accelerates speculative decoding by predicting multiple future positions in a single backbone pass, but on-device deployment constrains both drafter capacity and context storage. Under tight memory budgets, drafters must model long-range dependencies and fine-grained draft-position interactions without the growing KV-cache overhead of full-context attention. We propose HyFlash, a compact parallel drafter that introduces a prefix-memory prior to separate long-range context modeling from fine-grained draft-position interactions with limited capacity. Local attention captures recent context and draft-position interactions, while recurrent memory compresses historical target features into fixed-size states. This inductive bias enables effective local and long-range modeling with bounded draft-side memory. Experiments show that HyFlash achieves higher acceptance than full-context attention with substantially less KV storage and with larger gains for shallow drafters and long contexts.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
