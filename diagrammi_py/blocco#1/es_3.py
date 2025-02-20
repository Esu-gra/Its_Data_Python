#Calcolo della somma di numeri positivi

sum=0
i=1

for i in range(1,6):
    n=int(input("Inserire numero: "))
    if n > 0 :
        sum+=n
        i+=1
 
    else:
        i+=1
        continue
    if i == 5:
        print(sum)
        break