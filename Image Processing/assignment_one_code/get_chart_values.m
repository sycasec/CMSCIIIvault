% GET_CHART_VALUES(chart_image) - extract the 6x4 color values from the
% supplied colour chart image.
%
% Usage:
%         RGB_list = get_chart_values(chart_image)
%
% chart_image - NxMx3 array of uint8
% RGB_list - 24x3 element list of rgb values


function RGB_list = get_chart_values(chart_image)

% chart_image is assumed to be an RGB (0..255) image of the color test
% chart. The chart should consist of 4 rows of 6 color patches equally
% spaced. Here you simply need to obtain an RGB value for each patch and
% store it in an Nx3 table

% ---- INSERT YOUR CODE BELOW -----
final_r = 181 + 250 * 3;
final_c = 181 + 250 * 5;
x = chart_image(181:247:final_r, 181:245:final_c, :);
RGB_list = reshape(x, 24, 3);
% ---- INSERT YOUR CODE ABOVE -----

return
end






