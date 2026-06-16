# VisualClaw: A Real-Time, Personalized Agent for the Physical World

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.16295v1
- Published: 2026-06-15
- Updated: 2026-06-15
- Authors: Haoqin Tu, Jianwen Chen, Zijun Wang, Siwei Han, Juncheng Wu, Hardy Chen, Haonian Ji, Kaiwen Xiong, Jiaqi Liu, Peng Xia, Jieru Mei, Hongliang Fei, Jason Eshraghian, Zeyu Zheng, Yuyin Zhou, Huaxiu Yao, Cihang Xie
- Tags: agent, benchmark, context
- Categories: cs.CV, cs.CL
- URL: http://arxiv.org/abs/2606.16295v1

## One-Sentence Summary
Vision language models are serving as general-purpose interfaces for complex multimodal tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision language models are serving as general-purpose interfaces for complex multimodal tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, deployment still faces three gaps: VLMs typically incur high latency and cost when processing dense video frames and long prompts, the agent scaffold remains static after deployment, and standard video-QA...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CV, cs.CL

## Abstract Snapshot
Vision language models are serving as general-purpose interfaces for complex multimodal tasks. However, deployment still faces three gaps: VLMs typically incur high latency and cost when processing dense video frames and long prompts, the agent scaffold remains static after deployment, and standard video-QA benchmarks do not test whether agents can use visual evidence inside tool-using workspaces. We present VisualClaw, a self-evolving multimodal agent built around two principles. First, hybrid encoding reduces deployment cost by filtering less informative streaming frames with a cascaded gate and compressing the text skill bank through hot/cold top-k injection. Second, skill evolution lets the agent learn from failures: retrieved memories condition an evolver as direct concatenated context or as guided evidence, producing skill-bank updates that help future questions. Across 4 video-QA benchmarks with 2 VLMs, VisualClaw cuts per-question API cost by an average -98% versus full-frame upload and by -25.9% over the offline uniform 8 frame baseline, while boosting accuracy in most settings, e.g., an average +3.85% and a peak +15.80% on EgoSchema with Gemini 3 Flash. To address the gap, we curate VisualClawArena, a 200-scenario multimodal agentic benchmark built through a strict five-stage pipeline; models must use video evidence, documents, dynamic updates, and executable checks inside a workspace. On VisualClawArena, the same framework with computer-use agent backends improves macro accuracy by +2.9% for Codex (GPT-5.5) and +3.2% for Claude Code (Sonnet 4.6) over no-evolution baselines, with a -9.5% cost reduction compared to the uniform-sampled baseline. These properties make VisualClaw a natural fit for edge applications, where the cascade reduces a 1-hour streaming session from ~3,600 API uploads down to only 5-20 calls and the self-evolution makes it a perfect personalized assistant.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
