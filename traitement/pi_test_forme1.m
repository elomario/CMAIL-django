%version 7

function [f]= pi_test_forme1(filename)
%image=filename;
%form='jpg';
img = imread(filename); % lire l'image d�sir�e pour extraire les r�gions
bw = im2bw(img);
[labels, nbLabels] = bwlabel(img);   % �tiquetage des r�gions � l'aide de la fonction bwlabel
% region=1 et vide=0

% M�thode 2
for i=1:1
     %disp('for');
    [r,l] = find(labels==i);
    if length(find(labels==i)) > 20000 %taille minimum
        %length(find(labels==i))
        object = bwselect(bw,l,r);%on selectionne notre forme pour ne traiter que celle-ci
        %imtool(object)
        coin=regionprops(object,'Extrema');% je calcule les coins de ma forme ( positions )
        
        %verifier contient 4 coins
        
        %haut gauche
          %disp('if');
          
          temp=coin.Extrema(1,1);
          inf=temp-5;
          sup=temp+5;
          val=coin.Extrema(8,1);
          %---------------------------
          temp1=coin.Extrema(1,2);
          inf1=temp1-5;
          sup1=temp1+5;
          val1=coin.Extrema(8,2);
          
         if( inf<val && val<sup && inf1<val1 && val1<sup1)
            
        %if (coin.Extrema(1,1)==coin.Extrema(8,1)&& coin.Extrema(1,2)==coin.Extrema(8,2))
            
        
         temp=coin.Extrema(2,1);
          inf=temp-5;
          sup=temp+5;
          val=coin.Extrema(3,1);
          %---------------------------
          temp1=coin.Extrema(2,2);
          inf1=temp1-5;
          sup1=temp1+5;
          val1=coin.Extrema(3,2);
        
        
          
             %disp('if1');
              %haut droit
            %if (coin.Extrema(2,1)==coin.Extrema(3,1)&& coin.Extrema(2,2)==coin.Extrema(3,2))
             if( inf<val && val<sup && inf1<val1 && val1<sup1)
                 
                 
              temp=coin.Extrema(4,1);
              inf=temp-5;
              sup=temp+5;
              val=coin.Extrema(5,1);
              %---------------------------
              temp1=coin.Extrema(4,2);
              inf1=temp1-5;
              sup1=temp1+5;
              val1=coin.Extrema(5,2);

                 %disp('if2');
                  %bas droit
                %if (coin.Extrema(4,1)==coin.Extrema(5,1)&& coin.Extrema(4,2)==coin.Extrema(5,2))
                 if( inf<val && val<sup && inf1<val1 && val1<sup1)
                      temp=coin.Extrema(6,1);
                      inf=temp-5;
                      sup=temp+5;
                      val=coin.Extrema(7,1);
                      %---------------------------
                      temp1=coin.Extrema(6,2);
                      inf1=temp1-5;
                      sup1=temp1+5;
                      val1=coin.Extrema(7,2);

                
                    %bas gauche
                     %disp('if3');
                    %if (coin.Extrema(6,1)==coin.Extrema(7,1)&& coin.Extrema(6,2)==coin.Extrema(7,2))
                     if( inf<val && val<sup && inf1<val1 && val1<sup1)
                         
                        %disp('if4');
                        % distance entre Tl et Tr
                        d1=coin.Extrema(2,1)-coin.Extrema(1,1);
                        infd1=d1-5;
                        supd1=d1+5;
                        
                        % distance entre Tl et Tr
                        d2=coin.Extrema(5,2)-coin.Extrema(2,2);
                        infd2=d2-5;
                        supd2=d2+5;
                        % distance entre Tl et Tr
                        d3=coin.Extrema(5,1)-coin.Extrema(6,1);
                        infd3=d3-5;
                        supd3=d3+5;
                        % distance entre Tl et Tr
                        d4=coin.Extrema(6,2)-coin.Extrema(1,2);
                        %infd4=d4+5;
                        %supd4=d4+5;
                        
                        if (infd1<d2 && d2<supd1 && infd3<d4 && d4<supd3 && infd3<d2 && d2<supd3)
                            %disp('if5');
                        %if ( d1==d2 && d3==d4 && d3==d2)
                            
                            %disp('La forme est un colis sur l image');
                            f=2;
                            
                        elseif ( infd1<d3 && d3<supd1 && infd2<d4 && d4<supd2 )
                            %disp('if6');
                        %elseif ( d1 == d3 && d2==d4)
                            
                            %disp('La forme est une lettre ou un colis sur l image');
                            f=1;
                        else
                            
                           f=0;
                        end
                    else
                        %disp('La forme est particuli�re surment une pub');
                        f=0;
                    end
                else
                    %disp('La forme est particuli�re surment une pub');
                    f=0;
                end
            else
                %disp('La forme est particuli�re surment une pub');
                f=0;
            end
        else
            %disp('La forme est particuli�re surment une pub');
            f=0;
         end
    else
      f=3;  
    end  
    
end
