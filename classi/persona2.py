class Persona:
    def __init__(self):
        self.nome=""
        self.cognome=""
        self.età=0

    def disply_Data(self)->None:
        print(f"Nome: {self.nome}\n cognome: {self.cognome}\n età: {self.età}")

    #funzione che ci consenta di impostare il valore di self.nome
    # def setName(self,nome:str)->None:
    #     self.nome=nome

    def __str__(self):
        return f"Nome:{self.nome}"
    
    def setCognome(self,cognome:str)->None:
        self.cognome=cognome

    def setEtà(self,età:int)->None:
        if età < 0 or età>130:
            self.età=0
        else:
            self.età=età


  # funzione che mi  permette di ritornare del valore set.nome
    def getName(self)->str:
        return self.nome
  #funzione che mi consente di ritornare il valore di self.cognome

    def getCognome(self)->str:
        return self.cognome
    
   #funzione che mi consente di ritornare il valore di sel.età
    def getEtà(self)->int:
        return self.età