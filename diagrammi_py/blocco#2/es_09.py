
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






# #esercizio 18

# '''Scrivere un algoritmo che consenta all’utente di inserire una numero variabile di numeri interi (la quantità è scelta dall’utente). L'algoritmo deve:

# sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
# sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;
# Mostrare in output entrambe le somme e indicare quale somma è maggiore.'''

# i=0
# somma=0
# somma_pari=0
# somma_dispari=0

# while True:
#      x=input("Vuoi inserire il numero?").strip().lower()
#      if x=="no":
#           print(f"Non è stato inserito nesssun numero somma dei pari:{somma_pari} e la somma dei dispari: {somma_dispari}")
#      else:
#           n=int(input("inserire numero: "))
#           somma=somma+n
#           i=i+1
#           media=somma/i
#           if n%2==0 and n>media:
#                somma_pari=somma_pari+1
#           elif not(n%2==0) or n<media:
#                somma_dispari