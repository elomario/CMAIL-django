%version 7

function [f]= pi_test_forme1(filename)
%image=filename;
%form='jpg';
img = imread(filename); % lire l'image désirée pour extraire les régions
bw = im2bw(img);
[labels, nbLabels] = bwlabel(img);   % étiquetage des régions à l'aide de la fonction bwlabel
% region=1 et vide=0

% Méthode 2
for i=1:1
    %disp('for');
    [r,l] = find(labels==i);
    object = bwselect(bw,l,r);%on selectionne notre forme pour ne traiter que celle-ci
    imtool(object)
    %if length(find(labels==i)) >30000%taille minimum
    %if length(find(labels==i)) >100%taille minimum
    %length(find(labels==i))
    object = bwselect(bw,l,r);%on selectionne notre forme pour ne traiter que celle-ci
    %imtool(object)
    coin=regionprops(object,'Extrema');% je calcule les coins de ma forme ( positions )
    
    %verifier contient 4 coins
    f=0;
    xTL=coin.Extrema(1,1)
    yTL=coin.Extrema(1,2)
    xTR=coin.Extrema(2,1)
    yTR=coin.Extrema(2,2)
    xRT=coin.Extrema(3,1)
    yRT=coin.Extrema(3,2)
    xRB=coin.Extrema(4,1)
    yRB=coin.Extrema(4,2)
    xBR=coin.Extrema(5,1)
    yBR=coin.Extrema(5,2)
    xBL=coin.Extrema(6,1)
    yBL=coin.Extrema(6,2)
    xLB=coin.Extrema(7,1)
    yLB=coin.Extrema(7,2)
    xLT=coin.Extrema(8,1)
    yLT=coin.Extrema(8,2)
    
    
    
    %haut gauche Tl et LT
    disp('if');
    
    
    
    %---------------------------
    xTLinf=xTL-15;
    xTLsup=xTL+15;
    yTLinf=yTL-15;
    yTLsup=yTL+15;
    yBRsup=yBR+15;
    yBRinf=yBR-15;
    xRBsup=xRB+15;
    xRBinf=xRB-15;
    xLBsup=xLB+15;
    xLBinf=xLB-15;
    
    
    
    
    
    if( xTLinf<xLT && xLT<xTLsup && yTLinf<yLT && yLT<yTLsup)
        disp('ADRIEN CODE');
        
        %if (coin.Extrema(1,1)==coin.Extrema(8,1)&& coin.Extrema(1,2)==coin.Extrema(8,2))
        
        
        temp=coin.Extrema(2,1);
        inf=temp-15;
        sup=temp+15;
        val=coin.Extrema(3,1);
        %---------------------------
        temp1=coin.Extrema(2,2);
        inf1=temp1-15;
        sup1=temp1+15;
        val1=coin.Extrema(3,2);
        
        
        
        %disp('if1');
        %haut droit
        %if (coin.Extrema(2,1)==coin.Extrema(3,1)&& coin.Extrema(2,2)==coin.Extrema(3,2))
        if( inf<val && val<sup && inf1<val1 && val1<sup1)
            
            
            temp=coin.Extrema(4,1);
            inf=temp-15;
            sup=temp+15;
            val=coin.Extrema(5,1);
            %---------------------------
            temp1=coin.Extrema(4,2);
            inf1=temp1-15;
            sup1=temp1+15;
            val1=coin.Extrema(5,2);
            
            %disp('if2');
            %bas droit
            %if (coin.Extrema(4,1)==coin.Extrema(5,1)&& coin.Extrema(4,2)==coin.Extrema(5,2))
            if( inf<val && val<sup && inf1<val1 && val1<sup1)
                temp=coin.Extrema(6,1);
                inf=temp-15;
                sup=temp+15;
                val=coin.Extrema(7,1);
                %---------------------------
                temp1=coin.Extrema(6,2);
                inf1=temp1-15;
                sup1=temp1+15;
                val1=coin.Extrema(7,2);
                
                
                %bas gauche
                %disp('if3');
                %if (coin.Extrema(6,1)==coin.Extrema(7,1)&& coin.Extrema(6,2)==coin.Extrema(7,2))
                if( inf<val && val<sup && inf1<val1 && val1<sup1)
                    
                    %disp('if4');
                    % distance entre Tl et Tr
                    d1=coin.Extrema(2,1)-coin.Extrema(1,1)
                    infd1=d1-15;
                    supd1=d1+15;
                    
                    % distance entre Tl et Tr
                    d2=coin.Extrema(5,2)-coin.Extrema(2,2)
                    infd2=d2-15;
                    supd2=d2+15;
                    % distance entre Tl et Tr
                    d3=coin.Extrema(5,1)-coin.Extrema(6,1)
                    infd3=d3-15;
                    supd3=d3+15;
                    % distance entre Tl et Tr
                    d4=coin.Extrema(6,2)-coin.Extrema(1,2)
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
                    %disp('La forme est particulière surment une pub');
                    f=0;
                end
            else
                %disp('La forme est particulière surment une pub');
                f=0;
            end
        else
            %disp('La forme est particulière surment une pub');
            f=0;
        end
        
        
    elseif(yTR<yTLsup && yTR>yTLinf)
        disp('ALEX CODE');
        if(xRT<xRBsup && xRT>xRBinf)
            if(yBL<yBRsup && yBL>yBRinf)
                if(xLT<xLBsup && xLT>xLBinf)
                    disp('ALEX disdtqnce')
                    d1=yTR+yTL+xTL+xTR-xRT-yRT-xRB-yRB;
                    d2=xRT+xRB+yRT+yRB-xBL-yBL-xBR-yBR;
                    d3=xBL+yBL+xBR+yBR-xLT-yLT-yLB-xLB;
                    d4=xLT+yLT+xLB+yLB-xTL-yTL-xTR-yTR;
                    d1=abs(d1);
                    d2=abs(d2);
                    d3=abs(d3);
                    d4=abs(d4);
                    d1sup=d1+200;
                    d1inf=d1-200;
                    d2sup=d2+200;
                    d2inf=d2-200;
                    d2sup2=d2+120;
                    d2inf2=d2-120;
                    if(d3<d1sup && d3>d1inf)
                        disp('ALEX d#')
                        if(d4<d2sup && d4>d2inf)
                            disp('ALEX d2')
                            f=1;
                            if(d1>d2inf2 && d1<d2sup2)
                                f=2;
                            end
                        end
                    end
                end
            end
        end
    else
        disp('else finql')
        %disp('La forme est particulière surment une pub');
        f=0;
   
    end
    
    
end
%else
% f=3;
%end
end
