---
title: "Federated Unlearning: Guarantee the Right of Clients to Forget"
collection: publications
permalink: /publication/2022-10-25-Federated-Unlearning-Guarantee-the-Right-of-Clients-to-Forget
excerpt: 'This paper is about the federated unlearning.'
date: 2022-10-25
venue: 'IEEE Network (JCR-Q1)'
paperurl: 'https://ieeexplore.ieee.org/document/9964015/'
citation: '<b>Leijie Wu</b>, Song Guo, Junxiao Wang, Zicong Hong, Jie Zhang, and Yaohong Ding. &quot;Federated Unlearning: Guarantee the Right of Clients to Forget.&quot; <i>IEEE Network</i>. 2022.'
---

The Right to be Forgotten gives a data owner the right to revoke their data from an entity storing it. In the context of federated learning, the Right to be Forgotten requires that, in addition to the data itself, any influence of the data on the FL model must disappear, a process we call “federated unlearning.” The most straightforward and legitimate way to implement federated unlearning is to remove the revoked data and retrain the FL model from scratch. Yet the computational and time overhead associated with fully retraining FL models can be prohibitively expensive. In this article, we take the first step to comprehensively investigate the way to settle the unlearning paradigm in the context of federated learning. First, we define the problem of efficient federated unlearning, including its challenges and goals, and we identify three common types of federated unlearning requests: class unlearning, client unlearning, and sample unlearning. Based on those challenges and goals, a general pipeline is proposed for federated unlearning for the above three types of requests. We revisit how the training data affects the final FL model performance and thereby empowers the proposed framework with the reverse stochastic gradient ascent (SGA) and elastic weight consolidation (EWC). Various experiments are conducted to verify effectiveness of the proposed method in both aspects of unlearning efficacy and efficiency. We believe the proposed method will perform as an essential component for future machine unlearning systems.
