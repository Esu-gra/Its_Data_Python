'''
Crea una classe Book contenente i seguenti attributi: titolo,
autore, ISBN. La classe Book deve contenere i seguenti metodi:
__str__ , metodo per restituire una rappresentazione stringa del libro.
from_string , un metodo di classe per creare un'istanza di Book da 
una stringa nel formato "titolo, autore, isbn". Significa che è 
necessario utilizzare il riferimento di classe cls per creare un 
nuovo oggetto della classe Book utilizzando una stringa.

'''
class Book:
    def __init__(self,titolo:str,autere:str,isbn:str):
        self._titolo=titolo
        self._autere=autere
        self._isbn=isbn

    def __str__(self):
        return f"titolo:{self._titolo}\nautore:{self._autere}\nisbn:{self._isbn}"
    @classmethod
    def from_string(cls,s:str):
        titolo,autore,isbn=s.split(",")
        return cls(titolo,autore,isbn)



book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)
print(divina_commedia)