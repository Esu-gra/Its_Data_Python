from persona import Persona

class Dottore(Persona):
    _specializzazione:str
    _parcella:float
    def __init__(self,first_name, last_name,eta,parcella:float,specializzazione:str):
        self._specializzazione:str=self.set_special(specializzazione)
        self._parcella:float=self.set_parcella(parcella)
        

        super().__init__(first_name, last_name,eta)

    
    def set_special(self,sp:str):
        if isinstance(sp,str):
            self._specializzazione=sp
        else:
            self._specializzazione=None
            return "La specializzazione inserita non è una stringa!"
    
    def set_parcella(self,p:float):
        if isinstance(p,float):
            self._parcella=p
        else:
            self._parcella=None
            return "La parcella inserita non è un float!"
    
    def specializzazione(self)->str|None:
        return self._specializzazione
    
    def parcella(self)->float|None:
        return self._parcella

    
    def valid_doctor(self)->bool:
        if self._età>=30:
            print("Doctor nome e cognome is valid!")
            return True
        print("Doctor nome e cognome is not valid!")
        return False
    
    def doctorGreet(self)->str:
        return f"{self.greet()}  Sono un medico {self.specializzazione()}"
    

