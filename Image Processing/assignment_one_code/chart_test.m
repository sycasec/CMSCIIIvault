%
% A simple TEST for colorchart code
%

truecard = imread('color_testchart.jpg');
RGB_truechart = get_chart_values(truecard);

trueimage = imread('color_toys.jpg');   %<-- you can change this if you like

% -------------------------------------------------------------------------
% test example 1 - reduce all red tones by 50% (cyan colored)
badimage = trueimage;
badimage(:,:,1) = 0.5*badimage(:,:,1);
badimage(:,:,2) = 0*badimage(:,:,2);
badimage(:,:,3) = 0*badimage(:,:,3);
badtestcard = truecard;
badtestcard(:,:,1) = 0.5*badtestcard(:,:,1);
badtestcard(:,:,2) = 0*badtestcard(:,:,2);
badtestcard(:,:,3) = 0*badtestcard(:,:,3);

RGB_badchart = get_chart_values(badtestcard);
RGB_map = chart_correction(RGB_truechart,RGB_badchart);
fixedcard = apply_rgb_map(badtestcard,RGB_map);
fixedimage = apply_rgb_map(badimage,RGB_map);

figure
subplot(2,3,1); image(truecard);title('Reference Card');
subplot(2,3,2); image(badtestcard);title('Bad Card');
subplot(2,3,3); image(fixedcard);title('Fixed Card');
subplot(2,3,4); image(trueimage);title('Reference Image');
subplot(2,3,5); image(badimage);title('Bad Image');
subplot(2,3,6); image(fixedimage);title('Fixed Image');

% % -------------------------------------------------------------------------
% % test example 2 - reduce min max range and skew colors too (coffee
% % colored)
% badimage = trueimage;
% badimage(:,:,1) = 0.5*badimage(:,:,1);
% badimage(:,:,3) = 0.7*badimage(:,:,3);
% badimage = 0.5*badimage + 32;
% badtestcard = truecard;
% badtestcard(:,:,1) = 0.5*badtestcard(:,:,1);
% badtestcard(:,:,3) = 0.7*badtestcard(:,:,3);
% badtestcard = 0.5*badtestcard + 32;
% 
% RGB_badchart = get_chart_values(badtestcard);
% RGB_map = chart_correction(RGB_truechart,RGB_badchart);
% fixedcard = apply_rgb_map(badtestcard,RGB_map);
% fixedimage = apply_rgb_map(badimage,RGB_map);
% 
% figure
% subplot(2,3,1); image(truecard);title('Reference Card');
% subplot(2,3,2); image(badtestcard);title('Bad Card');
% subplot(2,3,3); image(fixedcard);title('Fixed Card');
% 
% subplot(2,3,4); image(trueimage);title('Reference Image');
% subplot(2,3,5); image(badimage);title('Bad Image');
% subplot(2,3,6); image(fixedimage);title('Fixed Image');
% 
% % -------------------------------------------------------------------------
% % >>>>>>>>>>>>>>>>>>>>>>>  additional testing <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
% % color_person 1: red and green channel scaling
% true_color_person = imread('color_person1.jpg');
% badimage = true_color_person;
% badimage(:,:,1) = 0.2*badimage(:,:,1);  %red shifted
% badimage(:,:,2) = 0.6*badimage(:,:,2);  %green shifted
% badimage = 0.7*badimage + 20;           %skew colors
% badtestcard = truecard;
% badtestcard(:,:,1) = 0.2*badtestcard(:,:,1);  %red shifted
% badtestcard(:,:,2) = 0.6*badtestcard(:,:,2);  %green shifted 
% badtestcard = 0.7*badtestcard + 20;            %skew colors
% 
% RGB_badchart = get_chart_values(badtestcard);
% RGB_map = chart_correction(RGB_truechart, RGB_badchart);
% fixedcard = apply_rgb_map(badtestcard, RGB_map);
% fixedimage = apply_rgb_map(badimage, RGB_map);
% 
% figure
% subplot(2,3,1); image(truecard);title('Reference Card');
% subplot(2,3,2); image(badtestcard);title('Bad Card');
% subplot(2,3,3); image(fixedcard);title('Fixed Card');
% 
% subplot(2,3,4); image(true_color_person);title('Reference Image');
% subplot(2,3,5); image(badimage);title('Bad Image');
% subplot(2,3,6); image(fixedimage);title('Fixed Image');
% 
% % ------------------------------------------------------------------------
% % color_person2: all channels scaled
% true_color_person = imread('color_person2.jpg');
% badimage = true_color_person;
% badimage(:,:,1) = 0.2*badimage(:,:,1); %red
% badimage(:,:,2) = 0.4*badimage(:,:,2); %green
% badimage(:,:,3) = 0.6*badimage(:,:,3); %blue
% badimage = 0.2*badimage + 36;           %skew colors
% badtestcard = truecard;
% badtestcard(:,:,1) = 0.2*badtestcard(:,:,1); %red
% badtestcard(:,:,2) = 0.4*badtestcard(:,:,2); %green
% badtestcard(:,:,3) = 0.6*badtestcard(:,:,3); %blue
% badtestcard = 0.2*badtestcard + 36;        %skew colors
% 
% RGB_badchart = get_chart_values(badtestcard);
% RGB_map = chart_correction(RGB_truechart, RGB_badchart);
% fixedcard = apply_rgb_map(badtestcard, RGB_map);
% fixedimage = apply_rgb_map(badimage, RGB_map);
% 
% figure
% subplot(2,3,1); image(truecard);title('Reference Card');
% subplot(2,3,2); image(badtestcard);title('Bad Card');
% subplot(2,3,3); image(fixedcard);title('Fixed Card');
% 
% subplot(2,3,4); image(true_color_person);title('Reference Image');
% subplot(2,3,5); image(badimage);title('Bad Image');
% subplot(2,3,6); image(fixedimage);title('Fixed Image');
