# Long-Term Memory-Guided Enhancement for Target Perception in Audio-Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36577v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Zhenhong Zhou, Xuanyue Zhao, Youji Liu, Yuanhe Zhang, Xiaoyu Ma, Lianyu Hu, Yang Liu
- Tags: long-term
- Categories: cs.SD, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.36577v1

## One-Sentence Summary
Audio large language models (ALLMs) can reason about the content of audio recordings to perform complex tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Audio large language models (ALLMs) can reason about the content of audio recordings to perform complex tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, these capabilities usually collapse in real-world environments when background noise and competing sources mix the target sound.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.SD, cs.AI, cs.CL

## Abstract Snapshot
Audio large language models (ALLMs) can reason about the content of audio recordings to perform complex tasks. However, these capabilities usually collapse in real-world environments when background noise and competing sources mix the target sound. Inspired by long-term memory in human listening, we propose Long-Term Memory-Guided Audio Enhancement (LTM-AE) to improve selective target perception by refining the audio representations of ALLMs without training. LTM-AE extracts representations in hidden states from separate clean reference recordings as long-term memory for each category, guiding enhancement toward a user-specified listening target. We reconstruct incoming audio tokens in the selected category long-term memory and interpolate the reconstructions with the original tokens before language backbone decoding. This interpolation controls the influence of stored auditory experience while keeping all ALLM parameters fixed. Diagnostic readouts across twenty sound categories and three ALLMs show that LTM-AE strengthens responses to a specified target amid three interfering sources. Averaged over constrained and free-form classification, accuracy gains over raw mixtures range from 29.53 to 46.15 percentage points across multiple open source models. For speech content recovery, LTM-AE with an additional learned token-level gate reduces Qwen2-Audio's word error rate from 23.07% to 14.77%. This work takes an initial step toward using principles of human long-term memory to enhance ALLMs for real-world listening. Our code is available at https://github.com/aynlp/ltm-audio-code

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
