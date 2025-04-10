'''
Verifica un CAP

Scrivi una funzione is_valid_cap(cap) 
che restituisce True se il CAP è valido (5 cifre),
 False altrimenti.
'''
import re 

def is_valide_cap(cap):
    # return bool(re.fullmatch(r"\d{5}",cap))
    cap=re.fullmatch(r"\d{5}",cap)
    if cap==cap:
        return True
    else:
        return False

print(is_valide_cap("12345"))