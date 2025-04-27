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
    def __init__(self, titolo: str, autore: str, stato_prestito: bool = False):
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito = stato_prestito

    def __str__(self):
        stato= "Disponibile" if not self.stato_prestito else "Prestato"
        return f"Titolo:{self.titolo}\nAutore:{self.autore}\nStato:{stato}"
    

class Biblioteca():
 
    def __init__(self):
     self.catalogo: list[Libro] = []

    
    def aggiungi_libro(self,libro:Libro):
            self.catalogo.append(libro)
            print(f"Libro aggiunto : {libro.titolo}")
           
   
    def presta_libro(self, titolo: str):
     for libro in self.catalogo:
        if libro.titolo == titolo:
            if not libro.stato_prestito:
                libro.stato_prestito = True
                print(f"Libro prestato: {titolo}")
            else:
                print(f"Il libro '{titolo}' è già stato prestato.")
            return
     print(f"Il libro '{titolo}' non è stato trovato.")
          
         
    def restituisci_libro(self, titolo: str):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.stato_prestito:
                    libro.stato_prestito = False
                    print(f"Libro restituito: {titolo}")
                else:
                    print(f"Il libro '{titolo}' non era stato prestato.")
                return
        print(f"Il libro '{titolo}' non è stato trovato.")

    def mostra_libri_disponibili(self):
        disponibili = [libro for libro in self.catalogo if not libro.stato_prestito]
        if disponibili:
            print("Libri disponibili:")
            for libro in disponibili:
                print(f"- {libro.titolo} di {libro.autore}")
        else:
            print("Nessun libro disponibile.")

 


biblioteca = Biblioteca()

# 2. Aggiungi libri
biblioteca.aggiungi_libro(Libro("Il Signore degli Anelli", "J.R.R. Tolkien"))
biblioteca.aggiungi_libro(Libro("1984", "George Orwell"))
biblioteca.aggiungi_libro(Libro("Harry Potter", "J.K. Rowling"))

# 3. Mostra i libri disponibili
biblioteca.mostra_libri_disponibili()

# 4. Presta un libro
biblioteca.presta_libro("1984")

# 5. Prova a prestare di nuovo lo stesso libro (errore)
biblioteca.presta_libro("1984")

# 6. Prova a prestare un libro inesistente (errore)
biblioteca.presta_libro("Il Piccolo Principe")

# 7. Mostra i libri disponibili
biblioteca.mostra_libri_disponibili()

# 8. Restituisci un libro
biblioteca.restituisci_libro("1984")

# 9. Prova a restituire di nuovo lo stesso libro (errore)
biblioteca.restituisci_libro("1984")

# 10. Prova a restituire un libro inesistente (errore)
biblioteca.restituisci_libro("Pinocchio")

# 11. Mostra i libri disponibili
biblioteca.mostra_libri_disponibili()

# 12. Stato finale dei libri
print("\n Stato finale dei libri:")
for libro in biblioteca.catalogo:
    print("-------------------")
    print(libro)