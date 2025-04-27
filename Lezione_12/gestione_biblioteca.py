'''
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione
di una biblioteca in Python. Il sistema deve permettere
di gestire un inventario di libri e le operazioni di prestito
e restituzione degli stessi. Gli utenti del sistema devono essere 
in grado di aggiungere libri al catalogo, prestarli, restituirli
e visualizzare quali libri sono disponibili in un dato momento.
'''

class Libro:
    def __init__(self,titolo:str,autore:str,stato_prestito:bool):
        self.titolo=titolo
        self.autore=autore
        self.stato_prestito=stato_prestito


    def __str__(self):
        stato= "Disponibile" if not self.stato_prestito else "Prestato"
        return f"Titolo:{self.titolo}\nAutore:{self.autore}\nStato:{stato}"
    

class Biblioteca(Libro):
 
    def __init__(self,libro:Libro):
        self.libro=libro
        self.catalogo:list=[]
    
    def aggiungi_libro(self,libro:Libro):
            self.catalogo.append(libro)
            print(f"Libro aggiunto : {libro.titolo}")
           
   
    def presta_libro(self,titolo):
     for titolo in self.catalogo:
        if self.libro.titolo==titolo:
            if not self.libro.stato_prestito:
                self.libro.stato_prestito = True
                print(f"Libro prestato: {titolo}")
            else:
                print(f" Il libro '{titolo}' è già stato prestato.")
            return
         
         

divina_com=Libro("Divina commedia","Dante Alighieri","Prsente")
print(divina_com)
