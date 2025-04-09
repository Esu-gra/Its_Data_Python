import random
punteggio=0
d1=random.randit(1,6)
d2=random.randit(1,6)
while True:
    if punteggio<100:
        d1
        d2
        if d1<0 and d1>=6 and d2<0 and d2>=6:
            d1
            d2
        else:
            sum=d1+d2
            if d1%2==0 and d2%2==0 and sum>8:
                punteggio=100
            else:
                if d1==6 or d2==6 or sum==7:
                    punteggio+=10
                else:
                    punteggio=0
                    print("Sconfitta")
                    break
    else:
        print("Vittoria")
        break
         
