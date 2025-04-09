n=int(input("inserire numero: "))

if n > 0:
    fattoriale=1
    i=1
    while True:
        if i == n:
            print(fattoriale)
            break
        else:
            i=i+1
            fattoriale=fattoriale*i
           

            