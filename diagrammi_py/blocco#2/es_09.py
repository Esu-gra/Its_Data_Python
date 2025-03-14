
# # Conteggio dei numeri divisibili
# #esercizio 9

n=int(input("inserire numero: "))

if n>0 and n%1==0:
     cont=0
     i=0
     for i in range(4):
          if i<=3:
               x=int(input("inserire numero da verificare: "))
               if x%n==0:
                    cont=cont+1
                    i+=1
     else:
           
          
                   
               print(cont)







# n=int(input("Inserire numero: "))
# i=0


# if n>0 :

#     count=0
#     for i in range(3) :
    
#        x=int(input("inserire numero: "))
#        if x%n==0:
#             count=count+1
            
#        print(count)
# else:
#      print("negativo")      




