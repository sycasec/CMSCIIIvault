% APPLY_RGB_MAP - replace R,G and B values in an image based
%  on the supplied lookup table
%
% Usage:
%          adjusted_image = apply_rgb_map(img,map)
%
% img -  NxMx3 uint8 image
% map -  256x3 lookup table for R,G,B values in range 0..255
%
% note R,G and B values are mapped independently. The RGB triples
% do not represent actual colours in the image (this is not a colormap).

function adjusted_image = apply_rgb_map(RGB_image,RGB_map)

% remap each RGB value in the current image onto a new image. Remember
% to treat each RGB channel separately. Also entry 1 in the table is
% colorlevel 0 and entry 256 is colorlevel 255

% ----- ADD YOUR CODE BELOW -----

adjusted_image = uint8(zeros(size(RGB_image)));

% Get the RGB values of the input image as 1D arrays
R = double(reshape(RGB_image(:,:,1), [], 1));
G = double(reshape(RGB_image(:,:,2), [], 1));
B = double(reshape(RGB_image(:,:,3), [], 1));

% copy individual R,G,B arrays of the map
R_new = max(min(round(RGB_map(R+1,1)), 255), 0);
G_new = max(min(round(RGB_map(G+1,2)), 255), 0);
B_new = max(min(round(RGB_map(B+1,3)), 255), 0);

% insert R,G,B arrays from map into image
adjusted_image(:,:,1) = reshape(R_new, size(RGB_image, 1), size(RGB_image, 2));
adjusted_image(:,:,2) = reshape(G_new, size(RGB_image, 1), size(RGB_image, 2));
adjusted_image(:,:,3) = reshape(B_new, size(RGB_image, 1), size(RGB_image, 2));

% ----- ADD YOUR CODE ABOVE -----

% resulting image must be uint8 with values in range 0..255
adjusted_image = uint8(adjusted_image);
return

end