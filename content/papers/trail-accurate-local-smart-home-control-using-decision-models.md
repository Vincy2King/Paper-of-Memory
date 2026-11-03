# Trail: Accurate Local Smart Home Control Using Decision Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.00610v1
- Published: 2026-10-31
- Updated: 2026-10-31
- Authors: Maleeha Masood, Deepak Vasisht, Indranil Gupta
- Tags: conversation
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2611.00610v1

## One-Sentence Summary
Natural-language driven smart home control remains challenging: cloud-hosted Large Language Models (LLMs) raise privacy concerns, while local Small Language Models (SLMs) can...

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Natural-language driven smart home control remains challenging: cloud-hosted Large Language Models (LLMs) raise privacy concerns, while local Small Language Models (SLMs) can generate invalid actions or misinterpret...

进一步看，论文的核心做法或实验重点可以概括为：We introduce Trail (Typed Registry-Anchored Inference for Language commands in Smart Homes), a fully local framework that replaces open-ended command generation with hierarchical typed decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Natural-language driven smart home control remains challenging: cloud-hosted Large Language Models (LLMs) raise privacy concerns, while local Small Language Models (SLMs) can generate invalid actions or misinterpret requests. We introduce Trail (Typed Registry-Anchored Inference for Language commands in Smart Homes), a fully local framework that replaces open-ended command generation with hierarchical typed decisions. Trail exploits the natural structure of a home's action space, selecting a room, device, and operation from candidates derived from the runtime device registry. This ensures valid actions while enabling confidence-based abstention when requests cannot be reliably resolved. We also design a structured memory module that uses typed decisions to support user preferences, device references, and multi-turn interactions. To evaluate Trail, we extend HomeBench and generate three datasets: Trek-Base, which tests natural-language variation; Trek-Robust, which evaluates robustness to changes in the home and its description; and Trek-Memory, which assesses conversational memory across multi-turn interactions. Trail achieves 85.3% accuracy on Trek-Robust versus 69.8% for a finetuned Qwen3.5-4B baseline, while remaining competitive on Trek-Base requests. With memory, Trail resolves 75.6% of the requests that depend on earlier turns, compared with 42.5% for the finetuned baseline given conversation history.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
