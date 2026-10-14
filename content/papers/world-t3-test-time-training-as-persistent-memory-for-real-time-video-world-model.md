# World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17434v1
- Published: 2026-10-12
- Updated: 2026-10-12
- Authors: Junyi Wu, Zekun Li, Chenhongyi Yang, Chen Guo, Lingchen Yang, Yongan Zhang, Xinyi Zhang, Hongbing Hu, Bartek Rymkowski, Srinath Sridhar, Yan Yan, Xijie Huang
- Tags: benchmark, context
- Categories: cs.CV, cs.AI, cs.MM
- URL: http://arxiv.org/abs/2610.17434v1

## One-Sentence Summary
Recent advances in video world models have enabled plausible interactive environments, yet long-horizon generation places a fundamental demand on visual memory: the previously...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in video world models have enabled plausible interactive environments, yet long-horizon generation places a fundamental demand on visual memory: the previously observed world must remain consistent as...

进一步看，论文的核心做法或实验重点可以概括为：Existing autoregressive approaches often implicitly rely on the generative model itself to retain such information, leading to spatial memory decay beyond the active context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CV, cs.AI, cs.MM

## Abstract Snapshot
Recent advances in video world models have enabled plausible interactive environments, yet long-horizon generation places a fundamental demand on visual memory: the previously observed world must remain consistent as the model continues to generate. Existing autoregressive approaches often implicitly rely on the generative model itself to retain such information, leading to spatial memory decay beyond the active context. We introduce World-T3, a camera-controlled video world model with a test-time training memory that consolidates past observations into dedicated model parameters. To robustly update this memory, we propose a recursive least-squares rule that incrementally absorbs novel visual features via online pose-keyed memory updates. Our TTT memory reads out previously observed scene features from the fast-weight state by camera pose, enabling consistent generation with constant storage and per-step computation regardless of rollout length. To facilitate real-time interactive generation with this robust memory, we further distill the autoregressive model into a few-step generator via dual-teacher distribution matching. On a long-horizon revisit benchmark, World-T3 raises revisit PSNR from 13.52 to 18.31 dB and reduces absolute rotation error from 3.344 to 1.075 relative to the strongest baseline on both metrics, while sustaining 20.6 FPS at 1280 x 704 on a single NVIDIA B200 GPU.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
