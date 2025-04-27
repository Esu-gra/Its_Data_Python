'''
Scrivi una funzione che accetti un dizionario di 
prodotti con i prezzi e restituisca un nuovo dizionario 
con solo i prodotti che hanno un prezzo superiore a 20,
ma scontati del 10%.
'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
   sconti={}
   for k,v in prodotti.items():
      if v>20:
       sconto=v*0.9
       sconti[k]=round(sconto,2)
      
   return sconti


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))