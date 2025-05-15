'''
Email semplici
Obiettivo: Definire pattern per email.


Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni,
 es. nome@dominio.co.uk.
'''


#Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.

import re
text='nome@dominio.com,nome@dominio.com.uk'

email=re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}',text)
print(email)