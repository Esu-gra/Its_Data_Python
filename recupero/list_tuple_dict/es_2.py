'''
Scrivi una funzione che prenda una lista di 
numeri e ritorni un dizionario che
classifichi i numeri in liste separate 
per numeri positivi e negativi.

'''

    
    
def positivi_negativi(lista:list)->dict:
    dic:dict={"positivi":[],"negativi":[]}
    for i in lista:
        if i >=0:
            dic["positivi"].append(i)
        else:
            dic["negativi"].append(i)

    return dic



        
print(positivi_negativi([12,-12,44,5,6,7,-5]))