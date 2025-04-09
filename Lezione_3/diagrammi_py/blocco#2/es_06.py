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
sum=0
if x>0:
    i=0
    while i<=3:

            n=int(input("inserire numero: "))
            i+=1
            if x%2==0:
                if n>(x/2):
                    
                    sum=sum+n
            
            else:
                if n<x:
                    
                    sum=sum+n
    print(sum)
                    
        
else:
    print("errore , x deve essere positivo")
            

