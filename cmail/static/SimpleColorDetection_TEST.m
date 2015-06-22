%BY C-MAIL TEAM..

function[couleur]= SimpleColorDetection_TEST(filename)


% clc;	% Clear command window.
% clear;	% Delete all variables.
% close all;	% Close all figure windows except those created by imtool.
% %imtool close all;	% Close all figure windows created by imtool.

% workspace;	% Make sure the workspace panel is showing.
% disp('2eme');
% % Change the current folder to the folder of this m-file.
% % (The "cd" line of code below is from Brett Shoelson of The Mathworks.)
% % if(~isdeployed)
% % 	cd(fileparts(which(mfilename))); % From Brett
% % end
% 
% %ver % Display user's toolboxes in their command window.
% 
% % % Introduce the demo, and ask user if they want to continue or exit.
% % message = sprintf('This demo will illustrate if the image is a PUB or a letter.\nDo you wish to continue?');
% % reply = questdlg(message, 'Run Demo?', 'OK','Cancel', 'OK');
% % if strcmpi(reply, 'Cancel')
% % 	% User canceled so exit.
% % 	return;
% % end
% %
% 
% try
%    disp('3eme');
%     close all;
%        
% 
     fontSize = 16;
%     % 	figure;
%     % 	% Maximize the figure.
%     % 	set(gcf, 'Position', get(0, 'ScreenSize'));
%     %
%     % 	% Change the current folder to the folder of this m-file.
%     % 	% (The line of code below is from Brett Shoelson of The Mathworks.)
%     % 	if(~isdeployed)
%     % 		cd(fileparts(which(mfilename)));
%     % 	end
%     
%     % Ask user if they want to use a demo image or their own image.
%     % 	message = sprintf('Do you want use a standard demo image,\nOr pick one of your own?');
%     % 	reply2 = questdlg(message, 'Which Image?', 'Demo','My Own', 'Demo');
%     % 	% Open an image.
%     % 	if strcmpi(reply2, 'Demo')
%     % 		% Read standard MATLAB demo image.
%     %         % fullImageFileName = 'peppers.png';
%     % 		message = sprintf('Which demo image do you want to use?');
%     % 		selectedImage = questdlg(message, 'Which Demo Image?', 'Onions', 'Peppers', 'Kids', 'Onions');
%     % 		if strcmp(selectedImage, 'Onions')
%     % 			fullImageFileName = 'onion.png';
%     % 		elseif strcmp(selectedImage, 'Peppers')
%     % 			fullImageFileName = 'peppers.png';
%     % 		else
%     % 			fullImageFileName = 'kids.tif';
%     % 		end
%     % 	else
%     % 		% They want to pick their own.
%     % 		% Change default directory to the one containing the standard demo images for the MATLAB Image Processing Toolbox.
%     % 		originalFolder = pwd;
%     % 		folder = 'C:\Program Files\MATLAB\R2010a\toolbox\images\imdemos';
%     %         %folder = ' /Users/badrhsaine/Desktop/Matlab_2014b/PI_test/MW_SimpleColorDetectionByHue/SimpleColorDetectionByHue.m*';
%     % 		if ~exist(folder, 'dir')
%     % 			folder = pwd;
%     % 		end
%     % 		cd(folder);
%     % 		% Browse for the image file.
%     % 		[baseFileName, folder] = uigetfile('*.*', 'Specify an image file');
%     % 		fullImageFileName = fullfile(folder, baseFileName);
%     % 		% Set current folder back to the original one.
%     % 		cd(originalFolder);
%     % 		selectedImage = 'My own image'; % Need for the if threshold selection statement later.
%     %
%     % 	end
%     %
%     % 	% Check to see that the image exists.  (Mainly to check on the demo images.)
%     % 	if ~exist(fullImageFileName, 'file')
%     % 		message = sprintf('This file does not exist:\n%s', fullImageFileName);
%     % 		uiwait(msgbox(message));
%     % 		return;
%     %     end
    
    [rgbImage, storedColorMap] = imread(filename);
    
    [rows, columns, numberOfColorBands] = size(rgbImage);
    
    
    if numberOfColorBands == 1
        if isempty(storedColorMap)
            % Just a simple gray level image, not indexed with a stored color map.
            % Create a 3D true color image where we copy the monochrome image into all 3 (R, G, & B) color planes.
            rgbImage = cat(3, rgbImage, rgbImage, rgbImage);
            
        else
            % It's an indexed image.
            rgbImage = ind2rgb(rgbImage, storedColorMap);
            % ind2rgb() will convert it to double and normalize it to the range 0-1.
            % Convert back to uint8 in the range 0-255, if needed.
            if eightBit
                rgbImage = uint8(255 * rgbImage);
            end
        end
    end
    
    % Display the original image.
    %subplot(3, 4, 1);
    %imshow(rgbImage);
%     drawnow; % Make it display immediately.
%     if numberOfColorBands > 1
%         title('Original Color Image', 'FontSize', fontSize);
%     else
%         %caption = sprintf('Original Indexed Image\n(converted to true color with its stored colormap)');
%         %title(caption, 'FontSize', fontSize);
%     end
    
    % Convert RGB image to HSV
    hsvImage = rgb2hsv(rgbImage);
    sImage = hsvImage(:,:,2);
    %subplot(3, 4, 3);
    %mshow(sImage);
    %title('Saturation Image', 'FontSize', fontSize);
    
    %---- Compute and plot the histogram of the "saturation" band------
    %hSaturationPlot = subplot(3, 4, 7);
    [saturationCounts, saturationBinValues] = imhist(sImage);
    maxSaturationBinValue = find(saturationCounts > 0, 1, 'last');
    maxCountSaturation = max(saturationCounts);
    %bar(saturationBinValues, saturationCounts, 'g', 'BarWidth', 0.95);
    %grid on;
    %xlabel('Saturation Value');
    %ylabel('Pixel Count');
    %title('Histogram of Saturation Image', 'FontSize', fontSize);
    
    %subplot(3, 4, 5);
    %grid on;
    %xlabel('Values');
    %ylabel('Pixel Count');
    %hold on;
    %plot(saturationBinValues, saturationCounts, 'g', 'LineWidth', 2);
    
    %disp(saturationCounts);
    count=0;
    couleur=0; % 0 it's pub / 1 it's a letter-colis / 2 indéterminée
    
    for i=1:size(saturationCounts)
        if(saturationCounts(i)>1000)
            count=count+1;
        end
    end
   disp('count =');
   disp(count);
    
   
  
   if(count<50)
        disp('colis');
        couleur=0;
   elseif(count<75)
        disp('vide');
        couleur=3;
   elseif(count<83)
        disp('letter');
        couleur=2;
   else
        disp('pub');
   end  
 
    
  
    
    
    
    
    
    
    
    
end

