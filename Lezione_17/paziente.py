from persona import Persona

class Paziente(Persona):
   _codice:str


   def __init__(self, first_name, last_name,eta,codice:str):
      self._codice:str=self.set_codice(codice)
      super().__init__(first_name, last_name)
      self.set_età(eta)
      self._codice=self.set_codice(codice)

    

   def set_codice(self,c):
        if isinstance(c,str):
            self._codice=c
        else:
            cod=str(c)
            self._codice=cod
    
   def codice(self)->str:
       return self._codice
   

   def paziente_info(self)->str:
       return f"Paziente: {self.name()} {self.last_name()}\nCodice:{self.codice()}"

        
      