'''
Esercizio 1: Creazione di una classe astratta con metodi astratti
Iniziamo definendo una classe base astratta chiamata Shape . 
Questa classe dovrebbe includere due metodi astratti : 
uno chiamato area , che sarà responsabile del calcolo dell'area 
di una forma, e un altro chiamato perimeter , che calcolerà il perimetro. Poiché Shape è astratta, non fornirà implementazioni specifiche per questi metodi. Invece, imposta un modello per tutte le forme che erediteranno da essa.

Quindi, create due sottoclassi concrete , Circle e Rectangle , 
che estendono entrambe la classe Shape . Ognuna di queste 
sottoclassi deve fornire la propria implementazione dei metodi 
area e perimetro , basata sulle formule geometriche appropriate 
alle proprie forme.

Infine , scrivi un semplice programma driver (codice di test)
che crei istanze di Circle e Rectangle , chiami i loro metodi area 
e perimetro e stampi i risultati. Questo ti aiuterà a verificare 
che la gerarchia delle classi funzioni come previsto.
'''
from abc import ABC,abstractmethod
import math
class Shape(ABC):
      @abstractmethod
      def area(self)->None:
            pass
      def perimeter(self)->None:
            pass


class Circle(Shape):
    
     def __init__(self,r):
           self.r=r
        
     def area(self):
           return f"Area :{math.pi*self.r**2}"
      
     def perimeter(self):
           return f"Perimetro: {2*math.pi * self.r}" 
     



c=Circle(5)
print(c.perimeter())
