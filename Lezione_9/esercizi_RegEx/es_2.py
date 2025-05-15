'''
 Riconoscere parole

Obiettivo: Lavorare con lettere e lunghezze di stringhe.

    Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
    Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
    Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.

'''
import re

#2.1
stri="ABBIAMO una parola o PIU parole MAIUSCOlE chrkcrhorhohpò2"
maiuscole:str=re.findall(r'\b[A-Z]{2,}',stri)

print(maiuscole)

#2.2
maiuscole_minuscole=re.findall(r"\b[A-Za-z]{2,}",stri)
print(maiuscole_minuscole)

#2.3

len_parola:list=re.findall(r'\b[a-zA-Z]{5,10}',stri)

print(len_parola)