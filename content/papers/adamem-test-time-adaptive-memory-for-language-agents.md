# AdaMEM: Test-Time Adaptive Memory for Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.05684v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Yunxiang Zhang, Yiheng Li, Ali Payani, Lu Wang
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.05684v1

## One-Sentence Summary
A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions.

进一步看，论文的核心做法或实验重点可以概括为：While recent work demonstrates the promise of agentic memory mechanisms, most systems restrict retrieval to episode initiation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions. While recent work demonstrates the promise of agentic memory mechanisms, most systems restrict retrieval to episode initiation. Consequently, agents are forced to rely on static guidance that becomes increasingly misaligned as long-horizon tasks unfold. To address this rigidity, we propose the Adaptive Memory Agent (AdaMEM), a novel framework for agent test-time adaptation. Without updating model parameters online, AdaMEM adapts agent behavior via a hybrid memory architecture: it maintains a long-term trajectory memory of raw experiences collected offline while generating dynamic short-term strategy memory on-the-fly to guide decision-making. This mechanism enables the trade-off between token efficiency and adaptability across varying inference-time compute levels. Empirically, AdaMEM significantly outperforms static memory baselines, achieving relative gains of up to 13% on ALFWorld and 11% on WebShop, with consistent leading performance extending to agentic search on HotpotQA. To further enhance this adaptation, we develop STEP-MFT, a Step-wise Memory Fine-Tuning technique that trains the policy to synthesize high-quality strategies from retrieved experiences, yielding additional performance gains. Our work establishes a new scaling dimension for agentic memory, supporting continuous reasoning and self-evolution post-deployment in real-world environments. Our code is available at https://github.com/yunx-z/AdaMEM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
