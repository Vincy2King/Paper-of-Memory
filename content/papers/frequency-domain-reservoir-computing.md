# Frequency Domain Reservoir Computing

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.24969v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Klaus Schertler, Xiomara Runge, Andrea Ceni, David Kappel, Claudio Gallicchio
- Tags: benchmark
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.24969v1

## One-Sentence Summary
While the quadratic sequence-length bottleneck of transformers has fueled a resurgence in recurrent models, effectively capturing complex dynamics requires architectures that...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While the quadratic sequence-length bottleneck of transformers has fueled a resurgence in recurrent models, effectively capturing complex dynamics requires architectures that balance efficient training with highly...

进一步看，论文的核心做法或实验重点可以概括为：Echo State Networks (ESNs) offer a compelling approach by utilizing fixed recurrent weights to circumvent backpropagation through time, enabling a closed-form training solution.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.LG

## Abstract Snapshot
While the quadratic sequence-length bottleneck of transformers has fueled a resurgence in recurrent models, effectively capturing complex dynamics requires architectures that balance efficient training with highly expressive latent states. Echo State Networks (ESNs) offer a compelling approach by utilizing fixed recurrent weights to circumvent backpropagation through time, enabling a closed-form training solution. However, achieving the expressivity needed for complex tasks demands large reservoirs, exposing an $\mathcal{O}(N^2)$ state-update bottleneck that prevents ESNs from matching the scale of contemporary recurrent models. To address this limitation, we introduce Frequency Domain Reservoir Computing (FRESCO), an ESN architecture operating entirely in the frequency domain while avoiding domain-shift overheads to achieve $\mathcal{O}(N)$ complexity for dense, non-linear recurrent updates. By employing a novel dimensional zero-padding input embedding, a packed \FDh readout, and a natively applied frequency-domain non-linearity, FRESCO drastically reduces computational costs and energy consumption of training and inference. Furthermore, FRESCO matches the state-of-the-art predictive performance on memory benchmarks, sequential classification, and multivariate long-horizon forecasting, offering a scalable path forward for dense recurrent architectures.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
