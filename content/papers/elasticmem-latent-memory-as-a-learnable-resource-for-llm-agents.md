# ElasticMem: Latent Memory as a Learnable Resource for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30690v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Tao Feng, Chongrui Ye, Tianyang Luo, Jingjun Xu, Xueqiang Xu, Haozhen Zhang, Ge Liu, Jiaxuan You
- Tags: agent, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.30690v1

## One-Sentence Summary
Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approaches concatenate retrieved memories into the context window, causing substantial token overhead and sensitivity...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience. However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approaches concatenate retrieved memories into the context window, causing substantial token overhead and sensitivity to noisy evidence, while latent-space approaches reduce textual cost but still rely on rigid retrieval or fixed-capacity memory interfaces. This creates a mismatch between query-dependent memory utility and fixed memory allocation. We propose ElasticMem, a memory-augmented LLM framework that learns to use memory as an elastic latent resource. ElasticMem builds an offline latent memory bank with retrieval keys and content caches, retrieves memories adaptively from the reasoner's hidden state, assigns each retrieved memory a variable latent budget through a learned policy, and injects selected latent states as soft memory tokens for generation. The full memory-use process is optimized with downstream task rewards through group-relative policy optimization. We evaluate ElasticMem on MemorySuite, covering memory-intensive QA and embodied agent control. Across Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct backbones, ElasticMem improves weighted average QA accuracy by 26.2% and 24.6%, and improves ALFWorld success rate by 66.3% and 27.2%, respectively, over the strongest baselines, while achieving the lowest ALFWorld token cost. Ablations and qualitative analyses further show that adaptive retrieval and elastic budget allocation help ElasticMem prioritize useful evidence and transferable plans beyond rigid cosine similarity. Our code for ElasticMem will be released at https://github.com/ulab-uiuc/ElasticMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
