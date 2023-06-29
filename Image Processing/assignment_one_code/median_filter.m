% MEDIAN_FILTER
%
% Usage:
%         med_img = median_filter(img,M,N)
%
% M,N size of MxN median filter to employ. 

function med_img = median_filter(img,M,N)

% ensure img is 0..1 and greyscale
img = im2double(img);
if (size(img,3)==3)
  img=rgb2gray(img);
end

% ----- INSERT YOUR OWN CODE BELOW -----
% 

% loopy solution
    % Padding the input image with zeros to handle boundary pixels
    padded_image = padarray(img,[floor(M/2), floor(N/2)],'symmetric');

    % Get the size of the input image and create an output image of the same size
    [rows,cols] = size(img);
    med_img = zeros(rows,cols);

    % Loop through each pixel in the input image and apply the median filter
    for i = 1:rows
        for j = 1:cols
            % Extract the MxN neighborhood centered around the current pixel
            neighborhood = padded_image(i:i+M-1, j:j+N-1);

            % Sort the values in the neighborhood
            sorted_neighborhood = sort(neighborhood(:));

            % Find the median value in the neighborhood
            if mod(M*N,2) == 1
                % Neighborhood size is odd
                median_value = sorted_neighborhood((M*N+1)/2);
            else
                % Neighborhood size is even
                median_value = (sorted_neighborhood(M*N/2) + sorted_neighborhood(M*N/2+1))/2;
            end

            % Assign the median value to the corresponding pixel in the output image
            med_img(i,j) = median_value;
        end
    end

    % Convert the output image to the same data type as the input image
    med_img = cast(med_img, class(img));

% Hint: the simplest solution is to use for loops and the sort() function
% to solve this. Consider also how you plan to deal with values near the
% boundary.


% ----- INSERT YOUR OWN CODE ABOVE -----

return
end




