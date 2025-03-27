# m = somma denaro depositato
# t= tempo 


def ammontare(m:float,t:int)->float:
    if m<=0:
        return 0
    elif t==0:
        return m
    else:
        return 1.005 * ammontare(m,t-1)
    


print(ammontare(100,12))