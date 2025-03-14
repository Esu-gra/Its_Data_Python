# ##Verifica se un numero è primo

# n=int(input("inserire numero: "))


# for i in len(n):
#     if n<2:
#         print("non è primo")
#     else:
#         div=2
#         if div<n:
#             if n%1==0:
#                 print("il numero non è primo")
#             else:
#                 div+=1
#         else:
#             print("il numero è primo")
         

#          #da finire##


n=int(input("inserire numero: "))
is_prime=True

while True:
    if n<2:
        is_prime=True
    else:
        div=2
        if div ==n:
            if n%div==0:
                is_prime=True
            else:
                is_prime=False
                div=div+1
    if is_prime==True:
        print("il numero è primo")
        break
    else:
        print("il numero non è primo")
        break