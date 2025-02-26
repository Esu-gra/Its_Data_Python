n1=int(input("inserire primo numero: "))
n2=int(input("inserire secondo numero: "))

if n1 > n2:
    n1,n2=n2,n1


prodotto=1

for n in range(n1,n2+1):
    prodotto=prodotto*n
print(f"il prodotto è {prodotto}")