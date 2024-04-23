---
title: "L4L: Experience-Driven Computational Resource Control in Federated Learning"
collection: publications
permalink: /publication/2021-03-23-L4L-Experience-Driven-Computational-Resource-Control-in-Federated-Learning
excerpt: 'This paper is about using deep reinforemecent learning to control the resource distribution in federated learning.'
date: 2021-03-23
venue: 'IEEE Transactions on Computers (TC) (CCF-A)'
paperurl: 'https://ieeexplore.ieee.org/document/9384231'
citation: 'Yufeng Zhan, Peng Li, Leijie Wu, and Song Guo. &quot;L4L: Experience-Driven Computational Resource Control in Federated Learning.&quot; <i>IEEE Transactions on Computers (TC)</i>. 2021.'
---

As the large-scale deployment of machine learning applications, there is much research attention on exploiting a vast amount of data stored on mobile clients. To preserve data privacy, federated learning has been proposed to enable large-scale machine learning by massive clients without exposing raw data. Existing works of federated learning struggle for accelerating the learning process, but ignore the energy efficiency that is critical for resource-constrained clients. In this article, we propose to improve the energy efficiency of federated learning by lowering CPU cycle frequencies of clients who are faster in the training group. Based on this idea, we formulate an optimization problem aiming to minimize the total system cost defined as a weighted sum of learning time and energy consumption. Due to the hardness of the formulated optimization problem and unpredictability of network quality, we propose L4L (Learning for Learning), an experience-driven computational resource control approach based on the deep reinforcement learning, which can derive the near-optimal solution with only the clients’ bandwidth information in the previous training rounds. We conduct the experiments using both real-world traces and synthetic traces to evaluate the proposed L4L approach. The results demonstrate the superiority of L4L as compared with the state-of-the-art solutions.
