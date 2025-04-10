'''
Verifica se una stringa è un numero intero

Scrivi una funzione is_integer(s) che restituisce 
True se la stringa è un numero intero (positivo o negativo), 
False altrimenti.
'''

import re



def pos_neg(s):

    return bool(re.fullmatch(r'-?\d+', s))
    
print(pos_neg("12"))
