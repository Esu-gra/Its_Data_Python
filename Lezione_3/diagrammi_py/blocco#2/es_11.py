'''
Classifica basata su più condizioni

Progettare un algoritmo che richieda all’utente di inserire un valore intero.
Il programma deve verificare:

se il numero è pari e maggiore di 10. Se sì, mostrare “Numero valido”;
se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”.
'''
n=int(input(" Inserire un numero: "))


if n%2==0 and n> 10: 
        print("Numero valido ")
else: 
        print("Numero non valido ")
    

#secondo metodo

# if n % 1==0:
#         if n%2 and n>10:
#                 print("numero  valido")
#         else:
#                 print("numero non valido")
# else:
#         n