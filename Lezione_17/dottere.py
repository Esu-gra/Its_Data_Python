from persona import Persona

class Dottore(Persona):
    _specializzazione:str
    _parcella:float
    def __init__(self,first_name, last_name,eta,specializzazione:str,parcella:float):
        super().__init__(first_name, last_name)
        self.set_età(eta)
        
        self._specializzazione=None
        self._parcella=None

        self.set_special(specializzazione)
        self.set_parcella(parcella)


    
    def set_special(self,sp:str):
        if isinstance(sp,str):
            self._specializzazione=sp
        else:
            print("La specializzazione inserita non è una stringa!")
    
    def set_parcella(self,p:float):
        if isinstance(p,float):
            self._parcella=p
        else:
            self._parcella=None
            print("La parcella inserita non è un float!")
    
    def specializzazione(self)->str|None:
        return self._specializzazione
    
    def parcella(self)->float|None:
        return self._parcella

    
    def valid_doctor(self)->bool:
        if self.età()!=None and self._età>=30:
            print(f"Doctor {self.name()} {self.last_name()} is valid!")
            return True
        print(f"Doctor {self.name()} {self.last_name()} non è valido")
        return False
    
    def doctorGreet(self)->str:
        print(f"{self.greet()}  Sono un medico {self.specializzazione()}")
    

