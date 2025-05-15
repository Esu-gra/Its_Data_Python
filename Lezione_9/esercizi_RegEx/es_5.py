'''
Riconoscere date
Obiettivo: Lavorare con formati numerici separati da caratteri speciali.


'''

import re 


#Esercizio 5.1: Scrivi una RegEx che riconosca una 
# data nel formato gg/mm/aaaa (es. 09/04/2025).
text="sono nato in data 09/04/2025 e  morto 12-4-2044"

data=re.findall(r"\d{2}/\d{2}/\d{4}",text)
print(data)




#Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.


data1= re.findall( r"\d{2}-\d{1,2}-\d{4}",text)

print(data1)