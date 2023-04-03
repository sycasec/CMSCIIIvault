[[ImageProcessingRoot]]

# Matlab Cheat Sheet

for when you forget the functions

`imread()` - reads image file
`im2gray()` - get grayscale
`imageVar(:,:,2);` → extracts the red color plane of the RGB image. 
`imhist(Image)` → display intensity histogram of an image
`imshowpair(image_1, image_2, kwargs)` → display pairs of images.
`imadjust(image)` → returns a contrast adjusted version of the image, only works for grayscale images.
`imlocalbrighten(image)` → adjust contrast of color image.