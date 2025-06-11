'''
Scrivi una funzione che accetti un dizionario 
di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo 
i prodotti che hanno un prezzo inferiore a 
50, ma
con i prezzi aumentati del 10% e arrotondati 
a due cifre decimali
'''

def new_dict(dic:dict)->dict:
    dic_1={}
    
    for k,v in dic.items():
        a=(10/100)*v
        if v < 50 : 
            prezzo_aumento=round(v*1.10,2)
            dic_1[k]=prezzo_aumento
    return dic_1

print(new_dict({"pane":12,"latte":55,"oro":34}))
        
