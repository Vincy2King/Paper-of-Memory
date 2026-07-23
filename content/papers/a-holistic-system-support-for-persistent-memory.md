# A Holistic System Support for Persistent Memory

- Source: OpenReview
- Venue: University of Virginia
- Paper ID: openreview:K49GvkMseM
- Published: 2022-08-01
- Updated: 2026-07-23
- Authors: {'fullname': 'Sihang Liu', 'username': '~Sihang_Liu1'}
- Tags: persistent memory
- Categories: OpenReview.net/Public_Article/ORCID.org/-/Record
- URL: https://openreview.net/forum?id=K49GvkMseM

## One-Sentence Summary
Persistent memory (PM) technologies, such as Intel’s Optane memory, unify memory and storage and deliver both data persistence and high-performance.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `University of Virginia` 这个 venue 相关。

从摘要来看，作者主要关注的是：Persistent memory (PM) technologies, such as Intel’s Optane memory, unify memory and storage and deliver both data persistence and high-performance.

进一步看，论文的核心做法或实验重点可以概括为：PM systems allow programs to directly manage their persistent data in memory, as opposed to the conventional way that goes through the file system.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：University of Virginia
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：OpenReview.net/Public_Article/ORCID.org/-/Record

## Abstract Snapshot
Persistent memory (PM) technologies, such as Intel’s Optane memory, unify memory and storage and deliver both data persistence and high-performance. PM systems allow programs to directly manage their persistent data in memory, as opposed to the conventional way that goes through the file system. Though performant, integrating this new memory technology would require significant changes throughout the system stack. First, programs that directly manage persistent data need to guarantee data recovery after a failure, as the file system is bypassed. However, it is hard and error-prone to ensure failure-recovery as programs need to carefully manage writes to PM. Second, PM is both a memory and a storage device, which requires various memory and storage supports, such as memory encryption and integrity verification that secure the data and memory deduplication for better bandwidth. Among these supports, the security guarantees are critical but can significantly increase the access latency. Moreover, these supports should also follow the existing crash consistency guarantees. Third, even with data encryption and integrity verification, there can be other vulnerabilities in a real PM system. For example, Intel’s Optane PM uses multiple levels of caches and buffers to improve performance, which can lead to new side channels. My thesis aims to provide system supports to overcome these new challenges. We hypothesize that a whole-system-level redesign, from programming support to hardware, that ensures correctness, security, and high-performance, is necessary in order to integrate persistent memory into practical systems. On the software side, to ensure the failure-recovery correctness, we have developed testing tools, PMTest and XFDetector, to help programmers detect failure-recovery issues; and a test case generator, PMFuzz, to generate high-coverage test cases. On the hardware side, we have proposed efficient and crash-consistent secured hardware-software co-designs for PM systems. Further on, we have reverse-engineered the commercial Optane PM from Intel, and exploited its covert and side-channel vulnerabilities.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
