% HISTEQ_CONTRAST - histogram equalisation for contrast enhancement
%
% Usage:
%         eq_img = histeq_contrast(img)
%
%  input image data is assumed to be in range 0..1

function eq_img = histeq_contrast(input_image)

% ----- INSERT YOUR CODE BELOW -----

% Convert the input image to a 256-level grayscale image
gray_image = uint8(input_image * 255);

% Calculate the histogram of the image
hist_result = hist(gray_image(:), 0:255);

% Calculate the cumulative distribution function (CDF)
cdf = cumsum(hist_result);

% Calculate the maximum value of the CDF
cdf_max = max(cdf);

% Calculate the equalization map
m = uint8((cdf / cdf_max) * 255);

% Replace the original pixel values with the equalized values using the lookup table
temp = m(gray_image + 1);

% Convert the image back to a double in the range 0.0 to 1.0
eq_img = double(temp) / 255;

% ----- INSERT YOUR CODE ABOVE -----

return
end