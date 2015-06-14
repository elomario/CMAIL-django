%version 7

function [s]= pi_test_forme1(filename)
%image=filename;
%form='jpg';
img = imread(filename); % lire l'image désirée pour extraire les régions
bw = im2bw(img);
[labels, nbLabels] = bwlabel(img);   % étiquetage des régions à l'aide de la fonction bwlabel
% region=1 et vide=0


% Méthode 2
for i=1:nbLabels
    [r,c] = find(labels==i);
    if length(find(labels==i)) > 15 %taille minimum
        %a=a+1;% On detecte une forme on accrémente
        object = bwselect(bw,c,r);%on selectionne notre forme pour ne traiter que celle-ci
        coin=regionprops(object,'Extrema');% je calcule les coins de ma forme ( positions )
        
        %verifier contient 4 coins
        
        %haut gauche
        if (coin.Extrema(1,1)==coin.Extrema(8,1)&& coin.Extrema(1,2)==coin.Extrema(8,2))
            
            %haut droit
            if (coin.Extrema(2,1)==coin.Extrema(3,1)&& coin.Extrema(2,2)==coin.Extrema(3,2))
                
                %bas droit
                if (coin.Extrema(4,1)==coin.Extrema(5,1)&& coin.Extrema(4,2)==coin.Extrema(5,2))
                    %bas gauche
                    if (coin.Extrema(6,1)==coin.Extrema(7,1)&& coin.Extrema(6,2)==coin.Extrema(7,2))
                        
                        % distance entre Tl et Tr
                        d1=coin.Extrema(2,1)-coin.Extrema(1,1);
                        % distance entre Tl et Tr
                        d2=coin.Extrema(5,2)-coin.Extrema(2,2);
                        % distance entre Tl et Tr
                        d3=coin.Extrema(5,1)-coin.Extrema(6,1);
                        % distance entre Tl et Tr
                        d4=coin.Extrema(6,2)-coin.Extrema(1,2);
                        
                        
                        if (d1==d2 && d3==d4 && d3==d2)
                            
                            disp('La forme est un colis sur l image');
                            s=2;
                            
                        elseif ( d1 == d3 && d2==d4)
                            
                            disp('La forme est une lettre ou un colis sur l image');
                            s=1;
                        end
                    else
                        disp('La forme est particulière surment une pub');
                        s=0;
                    end
                else
                    disp('La forme est particulière surment une pub');
                    s=0;
                end
            else
                disp('La forme est particulière surment une pub');
                s=0;
            end
        else
            disp('La forme est particulière surment une pub');
            s=0;
        end
    end
end
