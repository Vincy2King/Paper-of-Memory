# MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.21019v1
- Published: 2026-11-16
- Updated: 2026-11-16
- Authors: Ruiyang Jiang, Xinyang Liao, Weikai Huang, Yuqi Niu, Junjie Zhou, Yubin Zheng
- Tags: agent
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.21019v1

## One-Sentence Summary
Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown.

进一步看，论文的核心做法或实验重点可以概括为：When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, and the answer alone does not say where.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown. When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, and the answer alone does not say where. We formalize multimodal memory as four stages, Write, Update, Retrieve and Answer, and define nine error types across them. A stage-resolved analysis on Mem-Gallery traces most failures to a source stage, and most of those lie before the answer. Injecting known errors against fact-preserving control edits, we then follow each tainted record downstream. Early errors survive to the answer as apparent evidence, and hurt most when no other record holds the fact. A diagnosis that trusts the quoted evidence therefore blames the stage where the error surfaces, not the one where it began. We propose MemDoctor, in which the MLLM that built the memory diagnoses its own failures. It traces each needed fact backward through the four stages, accepts a diagnosis only when the cited evidence is found in memory, and repairs that stage before answering again. On a 4B backbone, MemDoctor improves accuracy on both Mem-Gallery and MemLens, outperforming all evaluated 8B baselines, and the same loop also improves MuRAG and A-Mem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
