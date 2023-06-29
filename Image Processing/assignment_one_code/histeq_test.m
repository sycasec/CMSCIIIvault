%
% EXAMPLE CODE FOR TESTING YOUR SOLUTIONS
%

% TRY DIFFERENT IMAGES AND CONTRAST CHNAGES FOR YOUR OWN TESTING
I1 = imread('vintage_postcard.tif');
%I2 = imread('pout.tif');
%I1 = imread('office_5.jpg'); I1=I1(:,:,2);
%I1 = imread('office_1.jpg'); I1=I1(:,:,2);
%I1 = imread('low_light.tif');
I1=im2double(I1);

% damage contrast
I1=0.8*I1;

I1eq = histeq_contrast(I1);
figure
subplot(1,2,1);
imshow(I1); caxis([0 1]); title('Test Image 1'); axis equal tight
subplot(1,2,2);
imshow(I1eq); caxis([0 1]); title('Histeq Result');  axis equal tight
colormap(gray);

fprintf(1,'Min/max of input image  1: %3.3f %3.3f\n', min(I1(:)),max(I1(:)) );
fprintf(1,'Min/max of output image 1: %3.3f %3.3f\n', min(I1eq(:)),max(I1eq(:)) );

% damage contrast
I2 = I1*0.25 + 0.25;
%I2 = I2 * 0.25 + 0.25;

I2eq = histeq_contrast(I2);
figure
subplot(1,2,1);
imagesc(I2); caxis([0 1]); title('Test Image 2');  axis equal tight
subplot(1,2,2);
imagesc(I2eq); caxis([0 1]); title('Histeq Result');  axis equal tight
colormap(gray);

fprintf(1,'Min/max of input image  2: %3.3f %3.3f\n', min(I2(:)),max(I2(:)) );
fprintf(1,'Min/max of output image 2: %3.3f %3.3f\n', min(I2eq(:)),max(I2eq(:)) );

% >>>>>>>>>>>>>>>>>>>>>>>>>> ADDITIONAL TESTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
% Test 3 - Pout.tif
% we will be converting the image to doubles first (0.0 -> 1.0)
I3 = imread('pout.tif');
I3 = im2double(I3);
I3 = I3*0.15 + 0.25;

I3eq = histeq_contrast(I3);
figure
subplot(1,2,1);imagesc(I3); caxis([0 1]);title('Test Image 3'); axis equal tight
subplot(1,2,2);imagesc(I3eq);caxis([0 1]);title('Histeq Result'); axis equal tight
colormap(gray);

% Test 4 - Office 5
I4 = imread('office_5.jpg');
I4 = I4(:,:,2);
I4 = im2double(I4);
I4 = I4*0.65; 

I4eq = histeq_contrast(I4);
figure
subplot(1,2,1);imagesc(I4); caxis([0 1]);title('Test Image 4'); axis equal tight
subplot(1,2,2);imagesc(I4eq);caxis([0 1]);title('Histeq Result'); axis equal tight
colormap(gray);

% Test 5 - low low_light
I5 = imread('low_light.tif');
I5 = im2double(I5);
I5 = I5*0.75 + 0.25;

I5eq = histeq_contrast(I5);
figure
subplot(1,2,1);imagesc(I5); caxis([0 1]);title('Test Image 5'); axis equal tight
subplot(1,2,2);imagesc(I5eq);caxis([0 1]);title('Histeq Result'); axis equal tight
colormap(gray);

% Test 6 - Office 1
I6 = imread('office_1.jpg'); I6=I6(:,:,2);
I6 = im2double(I6);
I6 = I6 * 0.69;

I6eq = histeq_contrast(I6);
figure
subplot(1,2,1);imagesc(I6); caxis([0 1]);title('Test Image 6'); axis equal tight
subplot(1,2,2);imagesc(I6eq);caxis([0 1]);title('Histeq Result'); axis equal tight
colormap(gray);
