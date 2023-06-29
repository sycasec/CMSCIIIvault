% SMART_BLUR - blur image to remove noise, but attempt to preserve
%  edge details where possible
%
% USAGE:
%   image_out = smart_blut( image_in , N , tolderance )
%
%    N         - size of NxN blur to apply to data (def. 5).
%    tolerance - estimate of gradient based on noise alone. Used to
%                contol weighting between oriignal and smoothed data
%                returned by function (def. 0.015)
%
% NOTE: all image data is converted to greyscale, with values in range 
%      0.0..1.0 before filtering is applied.

function B = smart_blur(I,N,tolerance)

% convert to greyscale 0.0..1.0
I =im2double(I);
if (size(I,3)==3)
  I=rgb2gray(I);
end

% handle missing input parameters
if (nargin<2)
  N=5;
  if (nargin<3)
    tolerance=0.015; % about 4 greylevels for 8bit data
  end
  if (nargin<1)
    error('This function requires an image as input');
  end
end

% ------ INSERT YOUR CODE BELOW ------

% creating the averaging filter
averaging_filter = ones(N)/N^2;

% creating the Sobel gradient filters
I_x = (1/240) * [-4   -5  0  5  4 ;
                 -8  -10  0 10  8 ; 
                 -10 -20  0 20 10 ;
                 -8  -10  0 10  8 ;
                 -4  -5   0  5  4];

I_y = (1/240) * [ 4   8  10   8  4; 
                  5  10  20  10  5; 
                  0   0   0   0  0; 
                 -5 -10 -20 -10 -5; 
                 -4  -8 -10  -8 -4];

% compute the x and y gradients
Gx = conv2(I, I_x, 'same');
Gy = conv2(I, I_y, 'same');

% compute the gradient magnitude using the provided equation
G = sqrt(Gx.^2 + Gy.^2);

%compute the weighing function for each pixel
W = min(tolerance./G, 1);

% blur the image with the averaging filter
B = conv2(I, averaging_filter, 'same');

% Construct the output image as combination of the blurred and original
% images

B = W.*B + (1.-W) .* I;

% ------ INSERT YOUR CODE ABOVE ------

return
end

