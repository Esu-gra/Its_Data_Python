'''
Scrivi una funzione che moltiplica tutti i 
numeri interi di una lista che sono minori di un
dato valore intero definito threshold

'''

def moltiplicazione(lista:list,threshold)->list:
   return [x*3 for x in lista if x<threshold]

print(moltiplicazione([122, 3, 4, 567, 888, 34, 6], 76))




