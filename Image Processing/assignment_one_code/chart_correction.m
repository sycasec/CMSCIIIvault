% CHART_CORRECTION - calculate RGB mappings to correct for color imbalance 
%                    between values measured from reference and test charts 
% Usage:
%         RGB_map = chart_correction(RGB_reference,RGB_measured)
%
% RGB_reference - Mx3 list of reference RGB samples 
% RGB_measured  - Mx3 list of actual RGB samples 
%
% RGB_map - 256x3 lookup table of R,G and B colour corrections
%

function RGB_map = chart_correction(RGB_reference,RGB_measured)

% Here we need to use the difference between the measured RGB values
% and the reference RGB values to create a lookup tables for RGB which will
% map the measured values back into the reference.

% Here the result is result is to be returned as a 256x3 table which contains the
% correction for the red,green and blue values
% good_values = double(RGB_reference)
% bad_values = double(RGB_measured)

% ---- INSERT YOUR CODE BELOW -----
% working solution
    % reshape to double because whiny function
    RGB_reference = double(RGB_reference);
    RGB_measured = double(RGB_measured);
   
    % guess in-between unknown points with linear regression estimate
    red_poly = polyfit(RGB_measured(:,1), RGB_reference(:,1), 1);
    green_poly = polyfit(RGB_measured(:,2), RGB_reference(:,2), 1);
    blue_poly = polyfit(RGB_measured(:,3), RGB_reference(:,3), 1);
    
    % Evaluate the polynomial at each RGB value from 0 to 255
    RGB_map(:,1) = polyval(red_poly, 0:255)';
    RGB_map(:,2) = polyval(green_poly, 0:255)';
    RGB_map(:,3) = polyval(blue_poly, 0:255)';

% trying interpolation, not working lmao
% RGB_reference_noisy = good_values + rand(size(good_values))*1e-6;
% RGB_map(:,1) = interp1(RGB_reference_noisy(:,1), bad_values(:,1), 0:255, 'linear', 'extrap') - (0:255)';
% RGB_map(:,2) = interp1(RGB_reference_noisy(:,2), bad_values(:,2), 0:255, 'linear', 'extrap') - (0:255)';
% RGB_map(:,3) = interp1(RGB_reference_noisy(:,3), bad_values(:,3), 0:255, 'linear', 'extrap') - (0:255)';

% HINT  - you can try and work these out from first principles or use interp1 or 
% polyfit/polyval to estimate the corrections from the measured to reference
% measurements for each of the values 0..255. Any fitted values outside 0..255 
% should be adjusted accordingly. Map values should be integers too.

% ---- INSERT YOUR CODE ABOVE -----           

return
end