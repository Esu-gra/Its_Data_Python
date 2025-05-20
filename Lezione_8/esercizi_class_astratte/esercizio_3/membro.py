'''
Crea una classe Libreria  con i seguenti attributi: libri, membri, 
totale_libri (ovvero, un attributo di classe per tenere traccia del 
numero totale di  istanze di Libro ). La classe Libreria deve 
contenere i seguenti metodi:
add_book , per aggiungere un libro alla biblioteca e incrementare total_books.
remove_bo:ok , per rimuovere un libro dalla biblioteca e decrementare total_books.
register_member , per aggiungere un membro alla libreria.
lend_book , per prestare un libro a un membro. Dovrebbe verificare 
se il libro è disponibile e se il membro è registrato.
__str__, metodo per restituire una rappresentazione stringa 
della biblioteca con l'elenco dei libri e dei membri.
library_statistics , un metodo di classe per stampare 
il numero totale di libri.


'''
from book import Book
class Libreria:
    totli_libri=0
    def __init__(self):
        self._libri=[]
        self._membri=[]

    def add_book(self,titolo):
        self._libri.append(titolo)
        self.__class__.totli_libri=+1
        return f"libro {titolo} aggiunto"

    def remove_book (self,titolo):
        if titolo in self.__class__.totli_libri:
            self._libri.remove(titolo)
            self.__class__.totli_libri=-1

            return "eliminato!"
        
        else:
            return "non esiste"
            
    def register_member(self,nome):
     if nome not in self._membri:
        self._membri.append(nome)
        return f"utente aggiunto"
     else:
         return "è gia registrato"
    
    def lend_book(self,libro,utente):
        if libro not in self._libri :
            return "libro non presente"
        if utente  in self._membri:
            return "utente non registrato"
        self._libri.remove(libro)
        self.__class__.totli_libri-=1
        return f"libro {libro} prestato a {utente}"


        
    def __str__(self):
        return f"Libri: {self._libri}\nMembri:{self._membri}"
    @classmethod
    def library_statistics(cls):
        return f"numero libri:{cls.totli_libri}"

lib = Libreria()
print(lib.add_book("1984"))
print(lib.add_book("Il piccolo principe"))
print(lib.register_member("Mario"))
print(lib.register_member("Luca"))
print(lib.lend_book("1984", "Mario"))
print(lib.lend_book("Il piccolo principe", "Anna")) 

print(lib)
print(Libreria.library_statistics())



