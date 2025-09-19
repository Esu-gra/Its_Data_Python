from film import Film

class Azione(Film):
    _genere:str="Azione"
    _penale:float=3


    def __init__(self, id, titolo):
        self._genere:str="Azione"
        self._penale:float=3


        super().__init__(id, titolo)

    
    def getGenere(self)->"Azione":
        return self._genere
    
    def getPenale(self)->float:
        return self._penale
    
    def calcolaPenaleRitardo(self,n_giorni:float)->float:
        return self._penale * n_giorni
    



class Commedia(Film):
    _genere:str="Commedia"
    _penale:float=2.50


    def __init__(self, id, titolo):
        self._genere:str="Commedia"
        self._penale:float=3


        super().__init__(id, titolo)

    
    def getGenere(self)->"Commedia":
        return self._genere
    
    def getPenale(self)->float:
        return self._penale
    
    def calcolaPenaleRitardo(self,n_giorni:float)->float:
        return self._penale * n_giorni
    



class Dramma(Film):
    _genere:str="Dramma"
    _penale:float=2.50


    def __init__(self, id, titolo):
        self._genere:str="Dramma"
        self._penale:float=3


        super().__init__(id, titolo)

    
    def getGenere(self)->"Dramma":
        return self._genere
    
    def getPenale(self)->float:
        return self._penale
    
    def calcolaPenaleRitardo(self,n_giorni:float)->float:
        return self._penale * n_giorni





    


    

    

    
