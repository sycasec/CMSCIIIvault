del Castillo, Kyle Adrian
BS Computer Science III-B
CMSC 194.1 - Research Internship I
# Optimization Research Group Annotated Bibliography 
---- 
Enkovaara, J. _et al._ (2011) “GPAW - massively parallel electronic structure calculations with python-based software,” _Procedia Computer Science_, 4, pp. 17–25. Available at: https\://doi.org/10.1016/j.procs.2011.04.003.

In this article, Enkovaraa and colleagues implements a massively parallel electronic structure simulation software using GPAW, which is an open source electronic structure library. The authors implemented this in a combination of C, CPython and Python. The authors then tested the overall performance of software and found that it performs within 25% of peak floating point performance. The authors have achieved this through the modification of CPython parallel import headers, allowing for a rapidly fast startup time.

An obvious limitation in this study is that the authors do not compare the performance of the newly developed simulation software against existing solutions. This is understandable, since most other simulation softwares are coded in compiled languages. The authors themselves noted that there is a need to utilize threading to increase the software's performance.

While this article provides interesting detail in the optimization of large-scale supercomputing software, it is unfortunately unrelated to my research interest and will not form the basis of my research.

---
Johnson, J.M. and Rahmat-samii, Y. (2002) “Genetic algorithm optimization and its application to antenna design,” _Proceedings of IEEE Antennas and Propagation Society International Symposium and URSI National Radio Science Meeting_, 1, pp. 326–329. Available at: https\://doi.org/10.1109/aps.1994.407746.

In this article, Johnson and Rahmat-samii present a novel (in 2002) optimization method called Genetic Algorithm (GA) optimization applied in antenna design. The authors first describe the various limitations of traditional optimization techniques and describe two designs, the first being unconstrained with varying amplitude and phase, and second with a constant amplitude. The authors then present a diagram of the GA optimizer developed for antenna design.

The obvious limitation of this article is that the authors do not present exact schematics of their design, and there is no testing data, nor any comparison data against existing solutions. This is probably due to patent limitations, which is understandable.

This article presents interesting information in the early roots of true random sampling, with the development and usage of a novel optimization method in antenna design. However, it is unrelated to my research topic.

---
Albacea, E.A. (1995) “Leapfrogging Samplesort,” _Algorithms, Concurrency and Knowledge_, 1023, pp. 1–9. Available at: https\://doi.org/10.1007/3-540-60688-2_30.

In this article, Albacea presents a Quicksort-based sorting algorithm that performs at $O(n(log n)^{2})$  at worst case, claiming that it is the most practical alternative to Quicksort. The author presents their analysis of the algorithm's performance at worst-case and average-case, concluding that the novel algorithm has better average comparisons and data interchanges than that required by the best implementation of Quicksort.

While this article is highly interesting in that there is a mathematical development creating more efficient sorting techniques, it unrelated to my research topic and will only serve as supplemental reading.