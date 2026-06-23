# Unlimited OCR Works

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.23050v1
- Published: 2026-06-22
- Updated: 2026-06-22
- Authors: Youyang Yin, Huanhuan Liu, YY, Qunyi Xie, Chaorun Liu, Shiqi Yang, Shaohua Wang, Zhanlong Liu, Hao Zou, Jinyue Chen, Shu Wei, Jingjing Wu, Mingxin Huang, Zhen Wu, Guibin Wang, Tengyu Du, Lei Jia
- Tags: compression
- Categories: cs.CV, cs.CL
- URL: http://arxiv.org/abs/2606.23050v1

## One-Sentence Summary
Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight.

进一步看，论文的核心做法或实验重点可以概括为：A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：working memory
- 来源分类信息：cs.CV, cs.CL

## Abstract Snapshot
Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However, the downside is equally evident: as the output sequence lengthens, the accumulated KV cache drives up memory consumption and progressively slows down generation. This stands in stark contrast to humans, who exhibit no such decline in efficiency during long-horizon copying tasks. In this technical report, we propose Unlimited OCR, a model designed to emulate human parsing working memory. Taking DeepSeek OCR as the baseline, we replace all attention layers in the decoder with our proposed Reference Sliding Window Attention (R-SWA), which reduces attention computation costs while maintaining a constant KV cache throughout the entire decoding process. By combining the high compression rate of DeepSeek OCR's encoder with our constant KV cache design, Unlimited OCR can transcribe dozens of pages of documents in a single forward pass under a standard maximum length of 32K. More importantly, R-SWA is a general-purpose parsing attention mechanism - beyond OCR, it is equally applicable to tasks such as ASR, translation, etc. Codes and model weights are publicly available at http://github.com/baidu/Unlimited-OCR.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
