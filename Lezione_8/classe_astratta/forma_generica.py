#una classe è astratta se ha almeno un metodo astratto

from abc import ABC,abstractmethod


class FormaGenerica(ABC):

    #metodo astratto 
    @abstractmethod
    def draw(self)->None:
        pass
        
    def setShape(self,shape:str)->None:
        if shape:
            self.shape=shape
        else:
            print("Errore!shape non puo essere una stringa vuota ")
    

    def getShape(self)->str:
        return self.shape