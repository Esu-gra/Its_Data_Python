from dottere import Dottore
from paziente import Paziente
class Fattura:
    _pazienti:list
    _dottore:Dottore
    _fatture:int

    def __init__(self,pazienti:list[Paziente],dottore:Dottore):
     if dottore.valid_doctor():
        self._pazienti:list=pazienti
        self._dottore:Dottore=dottore
        self._fatture:int=len(self._pazienti)
        self._salary:int=0
     else:
        self._pazienti=None
        self._dottore=None
        self._fatture=None
        self._salary=None
        print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    


    def get_salary(self)->float:
       return self._dottore.parcella() * len(self._pazienti)
    
    def get_fatture(self)->int:
       return self._fatture
    
    def addPaziente(self,new_p:Paziente):
      self._pazienti.append(new_p)
      self.get_fatture()
      self.get_fatture()
      print(f"Alla lista del Dottor cognome è stato aggiunto il paziente {new_p.codice()}")
    
    def removePaziente(self,idCode):
       codice=input("Codice: ")
       self._pazienti.remove(codice)
       self.get_fatture()
       self.get_salary()


