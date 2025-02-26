
numeri=[]

for i in range(5):
    while True:
        n=int(input("inserire numero compreso da 1 a 30: "))
        if i<=n<=30:
            numeri.append(n)
            break
        else:
            print(" numero non valido ")

for n in numeri:
    print("*"*n)