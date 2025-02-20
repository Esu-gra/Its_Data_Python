
#Trova il massimo tra 4 numeri:

max= int(input("inserire numero"))

i=0

while True:
    if i < 4:
        i+=1
        n=int(input("numero: "))
        if n>max:
            max=n
    else:
        print(max)
        break