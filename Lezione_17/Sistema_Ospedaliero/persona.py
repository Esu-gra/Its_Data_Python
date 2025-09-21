class Persona:
    _first_name:str
    _last_name:str
    _età:int

    def __init__(self,first_name:str,last_name:str):
      
        self.set_name(first_name)
        self.set_last_name(last_name)
        if self.name() and self.last_name():
            self._età=0
        else:
            self._età=None
        
    

    def set_name(self,n:str):
        if isinstance(n,str):
            self._first_name=n
        else:
            self._first_name=None
            print("Il nome inserito non è una stringa!")
    
    def set_last_name(self,l_n:str):
        if isinstance(l_n,str):
            self._last_name=l_n
        else:
            self._last_name=None
            print("Il nome inserito non è una stringa!")

    def set_età(self,age):
        if isinstance(age,int):
            self._età=age
        else:
            print("L'età deve essere un numero intero!")


    def name(self)->str|None:
        return self._first_name
    
    def last_name(self)->str|None:
        return self._last_name
    
    def età(self)->int|None:
        return self._età
    def greet(self)->str:
        return f"Ciao,sono {self.name()} {self.last_name()}!  Ho {self.età()} anni"