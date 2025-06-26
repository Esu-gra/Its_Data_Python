from frazioni import Frazione,semplificata
from fractionCompare import fractionCompare

l:list[Frazione]=[   1/2,   2/4,   3/5,   6/9,   4/7,   24/36,   12/36,   40/60,   5/11,   10/45,   42/78,   9/15]

    
   
          
        

l_s:list[Frazione]=semplificata(l)
equivalenti=True

if __name__ == "__main__":
    l = [Frazione(1,2),Frazione(2,4)]
    l_semplici = semplificata(l)
    fractionCompare(l, l_semplici)