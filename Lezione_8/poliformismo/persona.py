class Persona:
   
    #costruttore
    def __init__(self,nome:str,cognome:str,età:int):
        self.setNome(nome)
        self.setCognome(cognome)
        self.setEtà(età)


    def disply_Data(self)->None:
        print(f"Nome: {self.nome}\n cognome: {self.cognome}\n età: {self.età}")

    #funzione che ci consenta di impostare il valore di self.nome
    # def setName(self,nome:str)->None:
    #     self.nome=nome

    def setNome(self,nome):
        if nome:
            self.nome=nome
        else:
            print("Errore")
    
    def setCognome(self,cognome:str)->None:
        if cognome:
            self.cognome=cognome
        else:
            print("errore , strinfga vuota")

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
    

    def speak(self)->None:
        print(f"\nHello my name is {self.getName()}!\n")

    def __str__(self)->str:
       return f"\nHello {self.getName()}"