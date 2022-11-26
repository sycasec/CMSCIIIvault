[[MLRoot]]

Ramesh, A. _et al._ (2021) “Zero-Shot Text-to-Image Generation,” _Proceedings of the 38th International Conference on Machine Learning_,(139), pp. 8821-8831 Available from https://arxiv.org/pdf/2102.12092.pdf

In this article, Ramesh and colleagues design a Transformer based on attention mechanisms that autoregressively models text and image tokens as a single stream of data. The authors proceed to train the transformer on a the Conceptual Captions dataset, which consists of pairs of images and captions. After training, the model was evaluated by humans through voting, and was tested and compared against three existing Text-to-Image generation approaches. The authors found that their model obtains a Fréchet Inception Distance (FID) score on the MS-COCO dataset within 2 points of the best existing model. On the CUB-200 dataset, the authors' model obtains an FID score of 40 points less than the best existing model. The authors conclude that this simple approach for text-to-image generation performed in a large scale leads to improved generalization in terms of zero-shot performance relative to existing domain-specific approaches. 


However, the authors point out that their proposed zero-shot approach does not perform well on specialized distributions such as the CUB-200 dataset, and that fine-tuning of the model is a promising direction for improvement, and that improving generalization as a function of scale can be an essential driver in improving the approach.

While this article is highly informative and is definitely a good read, it will not form the basis of my research but only serve as a supplement, as it is not directly related to my research interest. 