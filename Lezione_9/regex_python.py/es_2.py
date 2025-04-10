'''
Trova tutte le email in un testo

Scrivi una funzione extract_emails(text) che prende 
un testo e restituisce tutte le email trovate.
'''
import re 

def extract_email(text):
    result:list[str]=re.findall(r'\S+@\S+',text)
    return result

print(extract_email("le email sono : esu@bbi.com , bbabbo@gmail.com"))