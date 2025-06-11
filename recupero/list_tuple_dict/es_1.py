'''
1) Scrivi una funzione che converta una lista 
di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore 
al valore già associato alla chiave.

'''

def tuple_in_dict(tup:tuple)->dict:
    dic:dict={}
    len_tup=len(tup)
    for i  in range(0 , len_tup,2):
        chiave=tup[i]
        valore=tup[i+1]
        dic[chiave]=valore
    return dic

print(tuple_in_dict(("cwl",12,"rerfe",3,"fver",6))  )  
