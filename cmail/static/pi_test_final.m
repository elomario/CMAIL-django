function [s]= pi_test_final(y,c)
temp=y;%FORME
temp1=c;%COULEUR


if (temp1==0)% trop couleur pub
    s=0; %pub
end

if (temp1==1) %valeur count faible =>lettres
    if(temp==1)% non rectangulaire
        s=1;%lettre
        
    end
    
    if(temp==2)%carré colis
        s=2;   
    end
    
end
end

