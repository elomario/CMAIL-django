%version 6

function [s]= pi_test_forme(filename)

img = imread(filename); % lire l'image désirée pour extraire les régions
bw = im2bw(img); % conversion dans une image binaire - fonction im2bw
%bw = ~bw;  % inversion des pixels (de l'image forme1) blanc => noir et vice-versa
[labels, nbLabels] = bwlabel(bw); % étiquetage des régions à l'aide de la fonction bwlabel
% region=1 et vide=0
disp(find(labels==8));
disp(length(find(labels==7)));
% Méthode 2
for i=1:nbLabels
    [r,l] = find(labels==i);
    object = bwselect(bw,l,r);%on selectionne notre forme pour ne traiter que celle-ci
    img_temp='temp.jpg';
    imwrite(object,img_temp);
    x=pi_test_forme1('temp.jpg');
    c=SimpleColorDetection_TEST(filename);
    s=pi_test_final(x,c);
	if (s==0)
		disp('pub');
	elseif (s==1)
		disp('lettre');
    elseif (s==2)
		disp('colis');
    else
        disp('undefined');
	end
end
