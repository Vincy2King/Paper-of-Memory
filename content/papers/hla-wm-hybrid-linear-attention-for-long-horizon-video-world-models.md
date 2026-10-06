# HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05739v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Zhuokun Chen, Feng Chen, Xi Lin, Xiyu Wu, Jiahao He, Jianfei Cai, Bohan Zhuang
- Tags: context, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2610.05739v1

## One-Sentence Summary
Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts.

进一步看，论文的核心做法或实验重点可以概括为：Softmax attention retains the full generation history through a growing KV cache, whereas recurrent linear attention compresses history into fixed-size states with substantially lower memory cost.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts. Softmax attention retains the full generation history through a growing KV cache, whereas recurrent linear attention compresses history into fixed-size states with substantially lower memory cost. However, we identify severe long-range forgetting in Gated DeltaNet (GDN), where information from distant but relevant scenes is progressively attenuated by subsequent state updates. To address this limitation, we propose HLA-WM, a training-free hybrid linear-attention framework that combines coarse-grained geometry-guided retrieval with fine-grained recurrent linear-state computation. HLA-WM exploits the affine structure of GDN to cache compact chunk-wise transition summaries, retrieve scene-relevant historical chunks using camera geometry, and recompose them into query-specific recurrent states. On the $60$-second SANA-WM-Bench, HLA-WM improves all six aggregate revisit-consistency and camera-control metrics of the base autoregressive generator without additional training, including a $0.74$ dB PSNR gain and a $28.5\%$ reduction in rotation error. The improvements persist after downstream refinement and generalize to MBench-A, where HLA-WM consistently improves all three revisit-consistency metrics across all four subsets and all evaluated inference modes over $547$ samples. At a $60$-second context, HLA-WM reduces historical-state memory by $12\times$ relative to full KV caching while incurring at most a $1.6\%$ reduction in inference throughput. These results demonstrate that selectively addressable recurrent memory can improve long-range scene recall while preserving the efficiency advantages of GDN. Project page: https://caesarhhh.github.io/hla-wm/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
