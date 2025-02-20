# x_pari=0
# x_dispari=0

# x=int(input("inserisci numero: "))

# i=1

# while True:
#     if i>0:
#         print("error ")
#         break
#     else:
#         n=int(input("inserire numeri: "))
#     if x%2==0:
#         somma=n

x=int(input("inserire un valore: "))
while True:
 if x > 0:
     i=0
     sum=0
     if i==5:
            print(sum)
            break
     else:
            n=int(input("inserire numero: "))
           
            if x % 2 == 0:
                if n > (x/2):
                    sum=sum+n
                else:
                    i=i+1
            else:
                if n < x:
                    sum = sum + n
                else:
                     i=i+1
 else:
     print("errore ,x deve essere positivo")
     break
   

#da completare 


