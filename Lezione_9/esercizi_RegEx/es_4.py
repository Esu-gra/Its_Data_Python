import re 

'''
CAP e codici
Obiettivo: Lavorare con lunghezze fisse e caratteri misti.


'''

#Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).

text=" abito in via ..... con cap 00124"
cap=re.findall(r'\b[0-9]{5}',text)
print(cap)

#Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato:
#6 lettere, 2 numeri, 1 lettera, 2 numeri.


text="il mio codice fiscale BNCMRA70A20H501B "
cf=re.findall(r'\b[A-Z]{3}[A-Z]{3}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z0-9]{4}[A-Z]{1}',text)
print(cf)