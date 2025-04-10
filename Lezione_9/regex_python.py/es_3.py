'''
Sostituisci tutti i numeri con ‘###’

Scrivi una funzione mask_numbers(text) che 
sostituisce tutte le sequenze di cifre con ###.
'''
import re 
def mask_number(text):
    mask:list[str]=re.sub(r"\d","#",text)
    return mask

print(mask_number("bbaboo12nato67"))