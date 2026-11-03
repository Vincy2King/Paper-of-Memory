# Neurons Are All You Need

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.00186v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Joseph B. Alzagatiti, Alain C. Glanzman, Perry A. Demsko, Pablo I. Salanova, David L. Glanzman
- Tags: persistent memory
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.00186v1

## One-Sentence Summary
For decades, artificial neural networks have operated under the assumption that durable, learned capability resides exclusively in adaptive synaptic parameters, primarily due to...

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：For decades, artificial neural networks have operated under the assumption that durable, learned capability resides exclusively in adaptive synaptic parameters, primarily due to the established neurobiology of...

进一步看，论文的核心做法或实验重点可以概括为：This design forces models to remain stateless during deployment, incurring well-known limitations such as catastrophic forgetting and expensive retraining.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
For decades, artificial neural networks have operated under the assumption that durable, learned capability resides exclusively in adaptive synaptic parameters, primarily due to the established neurobiology of synaptic connectivity. This design forces models to remain stateless during deployment, incurring well-known limitations such as catastrophic forgetting and expensive retraining. However, recent neurobiological research by Glanzman and colleagues, and others, shows that memories can be transferred between individual organisms in a synaptically independent manner. Inspired by this research, we sought to demonstrate memory transfer of persistent memory between AI model instances, leveraging a neurocentric version of memory. In this paper, we propose NURESA (Neural Unit with Retentive Self-Adaptive Architecture), a novel neural layer that eschews sole reliance on synaptic weight updating by introducing persistent intra-unit memory as a first-class, computational primitive. By structurally separating computation from persistent memory, NURESA enables autonomous memory accumulation and consolidation into transferable stores of memory registers. Experiments across MLP, GPT-2, and modern frontier models like Qwen2.5 demonstrate qualitatively new capability: zero-shot transfer of learned capability into a naive model instance without retraining or access to the original training data; this transfer is enabled by a sparse set of parameters in NURESA's memory register that the model selects on its own based on which neurons were most active. The memory transfer capability of NURESA also protects against domain loss when transformer models undergo learning via fine-tuning. Finally, the memory transfer process completes in approximately one minute even for transformer models with millions to billions of parameters, producing a transfer file orders of magnitude smaller than the original model.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
