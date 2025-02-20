
#Calcolo della somma dei quadrati fino a un numero intero positivo n



n=int(input("inserisci numero: "))

if n>0:
    sum=0
    i=1
    while True:
      if i>=n:
            print(sum)
            break
           
      else:
            sum=sum+(i*i)
            i=i+i
          

else:
   
    print("errore numero deve essere positivo")