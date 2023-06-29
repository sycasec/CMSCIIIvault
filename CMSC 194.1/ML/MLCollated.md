del Castillo, Kyle Adrian
BS Computer Science III-B
CMSC 194.1 - Research Internship I
# Machine Learning Annotated Bibliography 
---- 

Medalla, M.E. _et al._ (2021) “Relationship mapping of consumer buying behavior antecedents of secondhand clothing with Fuzzy DEMATEL,” _Journal of Management Analytics_, 8(3), pp. 530–568. Available at: https\://doi.org/10.1080/23270012.2020.1870878.

In this article, Medalla and colleagues review existing literature and identify several antecedents  to consumer buying behavior on second hand clothing (SHC). The authors invited 15 "experts" in SHC, all of which are 25-38 years old SHC buyers and users. These "experts" are asked to determine the influence of previously identified antecedents ins SHC buying. The authors then adopted a Fuzzified DEMATEL method to determine causal relationships between these antecedents based on the responses of "experts". The authors have concluded that the primary cause for SHC buying fall under *critical motivation*, and the primary effect is *economic motivation*.

A limitation easy to identify within this article is the credibility of "experts", where no seller was invited, being utilized as determinants in influence of antecedents. The results of the study then rely heavily on the opinions of said "experts". Furthermore, the article's conclusions are vague enough that they simply supplement obvious facts, such as wanting to buy SHC because of certain motivations.

While this study is an interesting application of computational intelligence as a supplement to the analysis of market trend and consumer behavior, this study will not be the basis of my research because I find that my interest lies elsewhere.

---

Ramesh, A. _et al._ (2021) “Zero-Shot Text-to-Image Generation,” _Proceedings of the 38th International Conference on Machine Learning_,(139), pp. 8821-8831 Available from https\://arxiv.org/pdf/2102.12092.pdf

In this article, Ramesh and colleagues design a Transformer based on attention mechanisms that autoregressively models text and image tokens as a single stream of data. The authors proceed to train the transformer on a the Conceptual Captions dataset, which consists of pairs of images and captions. After training, the model was evaluated by humans through voting, and was tested and compared against three existing Text-to-Image generation approaches. The authors found that their model obtains a Fréchet Inception Distance (FID) score on the MS-COCO dataset within 2 points of the best existing model. On the CUB-200 dataset, the authors' model obtains an FID score of 40 points less than the best existing model. The authors conclude that this simple approach for text-to-image generation performed in a large scale leads to improved generalization in terms of zero-shot performance relative to existing domain-specific approaches. 


However, the authors point out that their proposed zero-shot approach does not perform well on specialized distributions such as the CUB-200 dataset, and that fine-tuning of the model is a promising direction for improvement, and that improving generalization as a function of scale can be an essential driver in improving the approach.

While this article is highly informative and is definitely a good read, it will not form the basis of my research but only serve as a supplement, as it is not directly related to my research interest. 

<div style="page-break-after: always; visibilty: hidden">
</div>

---

Garcia-Garin, O. _et al._ (2021) “Automatic detection and quantification of floating marine macro-litter in aerial images: Introducing a novel deep learning approach connected to a web application in R,” _Environmental Pollution_, 273, p. 116490. Available at: https\://doi.org/10.1016/j.envpol.2021.116490.

In this article, Garin and colleagues developed a deep-learning model that uses convolutional neural networks (CNNs) to identify floating marine macro-litter (FMML) in aerial images of sea surfaces. The model was trained from aerial images obtained from photographic surveys performed by drones and manned aircraft between 2017 to 2019 over the Balearic Sea close to the shores of Spain. The authors then developed a Web Application to allow users to upload aerial images for the model to analyze. The authors found that the F1-score of their model was 8 points better than the best currently existing model.

The limitations in this article, as the authors themselves have identified, are related to the problems of computer vision. The authors found that environmental variables such as sun glint and sea surface perturbation introduces problems within the aerial images. 

This article presents an interesting application of Deep Learning and Artificial Intelligence towards the goal of bringing positive environmental change. However, this article does not specifically align with my research interest, and will serve as additional related literature.