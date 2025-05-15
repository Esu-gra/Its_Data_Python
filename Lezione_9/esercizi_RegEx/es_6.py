'''
Codici personalizzati
Obiettivo: Unire lettere, numeri e caratteri speciali.

Esercizio 6.1: Scrivi una RegEx per identificare un codice
prodotto nel formato PROD-1234-XY.

.
'''
import re
#Esercizio 6.1: Scrivi una RegEx per identificare un codice
#prodotto nel formato PROD-1234-XY.

text="prodotto nel formato PROD-1234-XY"

codice1=re.findall(r"[A-Z]{4}-[1-9]{4}-[A-Z]{2}",text)

print(codice1)



#Esercizio 6.2: Crea una RegEx per un ID alfanumerico di
#esattamente 8 caratteri,)

text2=" che può contenere lettere maiuscole e numeri  AB12CD34"

id=re.findall(r"[A-Z]{2}[1-9]{2}[A-Z]{2}[1-9]{2}",text2)
print(id)