---
title: "QuickDrop: Efficient Federated Unlearning via Synthetic Data Generation"
collection: publications
permalink: /publication/2024-12-02-QuickDrop-Efficient-Federated-Unlearning-via-Synthetic-Data-Generation
excerpt: 'This paper is about efficient federated unlearning.'
date: 2024-12-02
venue: 'Middleware24: Proceedings of the 25th International Middleware Conference'
paperurl: 'https://dl.acm.org/doi/10.1145/3652892.3700764'
citation: '<b>Leijie Wu</b>, Yaohong Ding, Akash Dhasade, Martijn De Vos, Anne-marie Kermarrec, Song Guo. &quot;QuickDrop: Efficient Federated Unlearning via Synthetic Data Generation.&quot; <i>Middleware24</i>. 2024.'
---


Federated Unlearning (FU) aims to delete specific training data from an ML model trained using Federated Learning (FL). However, existing FU methods suffer from inefficiencies due to the high costs associated with gradient recomputation and storage. This paper presents QuickDrop, an original and efficient FU approach designed to overcome these limitations. During model training, each client uses QuickDrop to generate a compact synthetic dataset, serving as a compressed representation of the gradient information utilized during training. This synthetic dataset facilitates fast gradient approximation, allowing rapid downstream unlearning at minimal storage cost. To unlearn some knowledge from the trained model, QuickDrop clients execute stochastic gradient ascent with samples from the synthetic datasets instead of the training dataset. The tiny volume of synthetic data significantly reduces computational overhead compared to conventional FU methods. Evaluations with three standard datasets and five baselines show that, with comparable accuracy guarantees, QuickDrop reduces the unlearning duration by 463× compared to retraining the model from scratch and 65 -- 218× compared to FU baselines. QuickDrop supports both class- and client-level unlearning, multiple unlearning requests, and relearning of previously erased data.
