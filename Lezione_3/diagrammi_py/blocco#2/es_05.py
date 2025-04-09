
#Calcolo della somma dei quadrati fino a un numero intero positivo n

n=int(input("inserire numero: "))


if n%1==0 and n>0:
      sum=0
      i=1
        
      while i <=n:
            sum=sum+(i*i)
            i+=1
      print(sum) 
            
      
  
else:
      print("erore n non un numero positivo ")

    
    