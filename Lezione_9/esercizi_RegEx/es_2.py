'''
 Riconoscere parole

Obiettivo: Lavorare con lettere e lunghezze di stringhe.

    Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
    Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
    Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.

'''
import re

#2.1
stri="ABBIAMO una parola o PIU parole MAIUSCOlE"
maiuscole:str=re.findall(r'\b[A-Z]{2,}',stri)

print(maiuscole)