'''
Scrivi una funzione che prende una lista di numeri
e ritorna un dizionario che classifica i numeri in 
liste separate per numeri pari e dispari.
'''

def classifica_numeri(lista:list) -> dict[str:list[int]]:
    lista_dict={'pari':[], 'dispari':[]}

    for n in lista:
        if n%2==0:
            lista_dict['pari'].append(n)
        else:
            lista_dict['dispari'].append(n)
    return lista_dict


print(classifica_numeri((12,34,5,56,7)))