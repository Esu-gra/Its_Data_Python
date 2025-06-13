'''
Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
'''
import string

def count_unique_words(text):
   text=text.translate(str.maketrans('', '', string.punctuation))
   text=text.lower()

   parole=text.split()
   dict={}
   for x in parole:
      if x in dict:
         dict[x]+=1
      else:
         dict[x]=1
   return dict


print(count_unique_words("Ciao a tutti? Perche non fare fare fare"))

   
      
    

    






