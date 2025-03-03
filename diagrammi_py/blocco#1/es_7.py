pari=0
dispari=0
i=0


for x in range(5):
    if i==4:
        print(pari)
        print(dispari)
        break
    else:
        n=int(input("inserire numero: "))
        if n%2==0:
            pari+=1
            i+=1
        else:
            dispari+=1
            i+=1
