# Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.28810v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Pedro H. Barcha Correia, Matheus Azevedo de Sá, Paulo H. Gomes de Senna, Giovanni Mandel Martignago, Victor Takashi Hayashi, Charles Christian Miers, Marcos A. Simplicio
- Tags: context, conversation, long-term
- Categories: cs.CR, cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2610.28810v1

## One-Sentence Summary
The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks.

进一步看，论文的核心做法或实验重点可以概括为：By embedding malicious instructions, these exploits manipulate language models to bypass intended behavior and operational boundaries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, long-term
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.CR, cs.AI, cs.CL, cs.LG

## Abstract Snapshot
The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks. By embedding malicious instructions, these exploits manipulate language models to bypass intended behavior and operational boundaries. In traditional chatbots, such attacks are confined to a single session because state memory is not preserved across conversations. However, persistent memory features in modern conversational interfaces enable cross-session attack propagation, establishing a threat vector known as memory injection. This work explores this emerging vulnerability in leading LLM-as-a-service platforms, highlighting its real-world severity and the need for countermeasures. While existing literature focuses on violations tailored to specific platform features, we present a general threat model. We demonstrate that all NIST attack goals are collectively achievable across ChatGPT Instant 5.3, Claude Sonnet 4.6, and Gemini 3 Flash under this model. We also show that memory injections can exploit multiple attack vectors, including personal memories, projects, skills, organization instructions, and Model Context Protocol (MCP)-connected resources. Our findings reveal that all evaluated services can be manipulated to persistently spread disinformation, generate harmful content, or simulate offline unresponsiveness, even in fresh sessions. In the particular case of Claude, shared-memory features allow an attacker to compromise multiple users within an organization and also exfiltrate user prompts. To address these vulnerabilities, we derive defense mechanisms from our proposed threat model and foundational cybersecurity principles. Our analysis indicates that nearly half of these mitigations remain unimplemented across the target services. Datasets and attack artifacts are available at https://github.com/PedroBarcha/Memory-injection.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
