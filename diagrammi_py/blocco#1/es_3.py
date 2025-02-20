#Calcolo della somma di numeri positivi

sum=0
i=1

for i in range(5):
    n=int(input("inserire numero: "))
    if n>0:
        sum+=n
        continue
    else:
        i+=1
        if i >=5:
            print(sum)
            break