'''
Riconoscere numeri

Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

    Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
    Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).

'''
import re
# 1.1
stringa="ciao i numeri sono 34 , non solo ma anche 234 ,-23 e -23"
nummbers:list[str]=re.findall(r'\d+',stringa)

#1.2
positivi_negativi:list[str]=re.findall(r'-?\d+',stringa)
print(nummbers)
print(positivi_negativi)