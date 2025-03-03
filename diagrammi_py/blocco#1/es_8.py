soglia=int(input("inserire la soglia: "))
i=0

for y in range(4):
    if i==3:
        break
    else:
        n=int(input("inserire numero: "))
        if n>soglia:
            print(n)
            i+=1
        else:
            i+=1