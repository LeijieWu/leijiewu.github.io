---
title: "Long-term Adaptive VCG Auction Mechanism for Sustainable Federated Learning with Periodical Client Shifting"
collection: Journals
permalink: /publication/2023-09-16-Long-Term-Adaptive-VCG-Auction-Mechanism-for-Sustainable-Federated-Learning-With-Periodical-Client-Shifting
excerpt: 'This paper is about the incentive mechanism design for federated learning.'
date: 2023-09-16
venue: 'IEEE Transactions on Mobile Computing (TMC)'
paperurl: 'http://academicpages.github.io/files/paper3.pdf'
citation: 'Leijie Wu, Song Guo, Yi Liu, Zicong Hong, Yufeng Zhan, and Wenchao Xu. &quot;Long-term Adaptive VCG Auction Mechanism for Sustainable Federated Learning with Periodical Client Shifting.&quot; <i>IEEE Transactions on Mobile Computing (TMC)</i>. (2023).'
---



Federated Learning (FL) system needs to incentivize clients since they may be reluctant to participate in the resource consuming process. Existing incentive mechanisms fail to construct a sustainable environment for the long-term development of FL system: 1) They seldom focus on system economic properties (e.g., social welfare, individual rationality, and incentive compatibility) to guarantee client attraction. 2) Current online auction modeling methods divide the whole continual process into multiple independent rounds and solve them one-by-one, which breaks the correlation between each round. Besides, the inherent characteristics of FL system (model-agnostic and privacy-sensitive) also prevent it from the optimal strategy by precise mathematical analysis. 3) Current system modelings ignore the practical problem of periodical client shifting, which cannot adaptively update its strategy to handle system dynamics. To overcome the above challenges, this paper proposes a long-term adaptive Vickrey–Clarke–Groves (VCG) auction mechanism for FL system, which incorporate a multi-branch deep reinforcement learning (DRL) algorithm. First, VCG auction is the only one that can simultaneously guarantee all crucial economic properties. Second, we extend the economic properties to long-term forms and apply the experience-driven DRL algorithm to directly obtain long-term optimal strategy, without any prior system knowledge. Third, we reconstruct a multi-branch DRL network to accommodate periodical client shifting by adaptive decision head switching for different time periods. Finally, we theoretically prove he extended economic properties (i.e., IC) and conduct extensive experiments on several real-world datasets. Compared with state-of-the-art approaches, the long-term social welfare of FL system increases by 36% with a 37% reduction in payment. Besides, the multi-branch network can adaptively handle periodical client shifting on the timeline.
