'''
Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
'''
from string import punctuation


def count_unique_words(text:str)->dict[str,int]:
   text=text.translate(str.maketrans('', '', punctuation))
   text=text.lower()

   parole=text.split()
   d:dict={}
   for x in parole:
      if x in d:
         d[x]+=1
      else:
         d[x]=1
   return d




   
      
    

    
def count_text(text:str)->dict[str,int]:
   d:dict[str,int]={}
   l_text:str=text.lower()
   tokens:list[str]=l_text.split()

   for token in tokens:
      c_token=""
      for c in token:
         if c.isalpha() or c.isdigit():
            c_token+=c
         if not c_token:
            continue
         if c_token in d:
            d[c_token]+=1
         else:
            d[c_token]=1
   return d
    

   






print(count_text("Ci.ao a tutti?!11 Perche non fare fare farea"))