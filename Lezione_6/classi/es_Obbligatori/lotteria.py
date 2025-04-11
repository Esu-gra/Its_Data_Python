import random

class LotteriaMacchina:
    def __init__(self,lotto:list=None):
     if lotto is None:
        self.lotto=[1,2,3,4,5,6,7,8,9,10,"a","d","f"]
     else:
        self.lotto=lotto
     self.biglietto_vincente=[]



    def tenta_fortuna(self):
        self.biglietto_vincente=random.sample(self.lotto,4)
        return self.biglietto_vincente
    
    def messagio_vincente(self):
    
        print(f"{self.biglietto_vincente}: vinve 100 mila euro") 


lotteria=LotteriaMacchina()
vincita=lotteria.tenta_fortuna()
lotteria.messagio_vincente()
   



