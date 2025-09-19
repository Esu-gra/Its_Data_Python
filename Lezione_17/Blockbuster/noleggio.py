
from movie_genre import *

class Noleggio:
    _film_list:list=[Azione,Dramma,Commedia]
    _rented_film:dict
    

    def __init__(self,film_list:list,):
        self._film_list=film_list
        self._rented_film={int:list}

    
    def isAvaible(self,film)->bool:
        if film in self._film_list:
            print(f"Il film scelto è disponibile: {film}!")
            return True
        
        else:
            print(f"Il film scelto non è disponibile: {film}!")
            False
    

    def rentAMovie(self,film,clientID):
        if film in self._film_list:
            self._film_list.remove(film)
            self._rented_film[clientID]=[]
            print(f"Il cliente {clientID} ha noleggiato {film}!")
        else:
            print(f"Non è possibile nolegiare il film {film}!")
        
    
    def givBack(self,film,clientID,days:float):
        if film not in self._film_list:
            self._film_list.append(film)
            self._rented_film[clientID]=film
            if isinstance(film,Azione):
                film.calcolaPenaleRitardo(days)
            elif isinstance(film,Commedia):
                film.calcolaPenaleRitardo(film)
            else:
                film=Dramma
                film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film} e' di {film._penale} euro!")
                 

            

        



        