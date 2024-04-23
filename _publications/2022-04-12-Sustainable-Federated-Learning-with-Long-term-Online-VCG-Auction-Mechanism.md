---
title: "Sustainable Federated Learning with Long-term Online VCG Auction Mechanism"
collection: publications
permalink: /publication/2022-04-12-Sustainable-Federated-Learning-with-Long-term-Online-VCG-Auction-Mechanism.md
excerpt: 'This paper is about the long-term incentive mechanism design for federated learning.'
date: 2022-04-12
venue: 'IEEE 42nd International Conference on Distributed Computing Systems (ICDCS)'
paperurl: 'https://ieeexplore.ieee.org/document/9912254'
citation: 'Leijie Wu, Song Guo, Yi Liu, Zicong Hong, Yufeng Zhan, and Wenchao Xu. &quot;Sustainable Federated Learning with Long-term Online VCG Auction Mechanism.&quot; <i>IEEE 42nd International Conference on Distributed Computing Systems (ICDCS)</i>. 2022: 895-905. (CCF-B).'
---


Federated learning (FL) clients may be reluctant to participate in the energy-consuming FL unless they are incentivized. Existing incentive mechanisms seldom consider the economic properties, e.g., social welfare, individual rationality and incentive compatibility, which significantly limits the sustainability of FL to attract more clients. The Vickrey–Clarke–Groves (VCG) auction is an ideal mechanism for simultaneously guaranteeing all crucial economic properties to maximize social welfare. However, VCG auction cannot be applied directly to FL scenarios due to the following challenges: 1) It requires precise analytical derivation of the optimal strategy, which is unavailable due to the inherent model-unknown and privacy-sensitive characteristics of FL. 2) Current auction modeling decomposes the entire process into multiple independent rounds and solves them one-by-one, which breaks the successive correlation between rounds in the long-term training process of FL. To overcome these challenges, this paper presents a long-term online VCG auction mechanism for FL that employs an experience-driven deep reinforcement learning algorithm to obtain the optimal strategy. Besides, we extend long-term forms of the crucial economic properties for the successive FL process. Furthermore, knowledge transfer is applied to reduce the excessive training overhead arising from the VCG payment rules. By exploiting the environmental similarity among sub-auctions, we develop the strategy sharing to significantly cut the training time by half. Finally, we theoretically prove the extended economic properties and conduct extensive experiments on multiple real-world datasets. Compared with state-of-the-art approaches, the long-term social welfare of FL increases by 36% with a 37% reduction in payment.
