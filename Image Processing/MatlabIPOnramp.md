# Matlab Image Processing Onramp

```toc
```

## Contrast and Intensity Histograms
- an intensity histogram separates pixels into bins based on their intensity values
- dark images have many pixels binned in the low end of the histogram
- bright images have many pixels binned at the high end of the histogram
- ![[Pasted image 20230222204757.png|475]]

- `imhist(Image)` → displays intensity histogram of an image. Use this to investigate contrast in an image.
- 