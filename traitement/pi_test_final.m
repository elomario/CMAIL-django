function [s]= pi_test_final(y,c)
temp=y;%FORME
temp1=c;%COULEUR


if (temp1==0)% trop couleur pub
    s=0; %pub
end

if (temp1==1) %valeur count faible =>lettres
    if(temp==0)% non rectangulaire
        s=0;%pub
        
    end
    if(temp==1)%rectangulaire LETTRES
        s=1;
        
    end
    if(temp==2)%carré colis
        s=2;   
    end
    if(temp==3)%indeterminé
        s=3;   
    end
    if(temp==4)%test ta mere
        s=4;   
    end
    
end


