
    


# c=Creatura("Aldo")
# c.setNome(1234)
# print(c.getName())







         #### Aleno ####

from random import randint

class Creatura:
    def __init__(self,nome:str):
        self.setNome(nome)


    def setNome(self,nome:str):
        if  not isinstance(nome,str):
            self.nome="Creatura Generica"
        else:
            self.nome=nome
    
    def getNome(self):
        return self.nome
    
    def __str__(self):
        return f"Creatura: {self.getNome()}"


import random

class Alieno(Creatura):
    def __init__(self):
        self.setMatricola()    
        self.setMunizioni()      
        nome_atteso = f"Robot-{self.matricola}"
        super().__init__(nome_atteso) 

    def setMatricola(self):
        self.matricola = random.randint(10000, 90000)

    def getMatricola(self):
        return self.matricola

    def setMunizioni(self):
        self.munizioni = [i**2 for i in range(15)]

    def getMunizioni(self):
        return self.munizioni

    def __str__(self):
        return f"Alieno: {self.getNome()}"






           ### Mostro ###

class Mostro(Creatura):
    def __init__(self, nome,urlo_vittoria:str,gemito_sconfitta:str):
        super().__init__(nome)
        self.setVittoria(urlo_vittoria)
        self.setSconfitta(gemito_sconfitta)
        self.setAssalto()
    
    def setAssalto(self):
        self.assalto=random.sample(range(1,101),15)

    def setVittoria(self,vittoria:str):
        if  not isinstance(vittoria,str):
            self.urlo_vittoria= "GRAAAHHH" 
        else:
            self.urlo_vittoria=vittoria

    def setSconfitta(self,sconfitta:str):
        if not isinstance(sconfitta,str):
            self.gemito_sconfitta="Uuurghhh"
        else:
            self.gemito_sconfitta=sconfitta
    

    def getUrloVittoria(self):
        return self.urlo_vittoria
    
    def getGemitoSconfitta(self):
        return self.gemito_sconfitta
    
    def getAssalto(self):
        return self.assalto
    


    def __str__(self):
        return f"Mostro: {self.nome.swapcase()} "


    

'''
pariUguali(a: list[int], b: list[int]). 
Questo metodo riceve in input due liste a e b 
di interi positivi e deve restituire una lista c.
'''
def pariUguali(a:list[int],b:list[int])->list:
     return [1 if x % 2 == 0 and y % 2 == 0 else 0 for x, y in zip(a, b)]


#### funzioneCombattimento ###

def combattimento(a:Alieno,m:Mostro):
    if not isinstance(a,Alieno) or not isinstance(m,Mostro):
        return None
    munizioni=a.getMunizioni()
    assalto=m.getAssalto()

    esito=pariUguali(munizioni,assalto)
    contatore=esito.count(1)

    if contatore > 4 :
        for _ in range(3):
            print(m.getUrloVittoria())
        return m
    
    else:
        print(m.getGemitoSconfitta())
        return a


def proclamaVincitore(c:Creatura):
    if isinstance(c,Alieno):
        print("\n **Alieni** hanno vinto!\n")
    elif isinstance(c,Mostro):
        print("\n **Mostri** hanno vinto!\n ")
    else:
        print("\n Creatura generica\n")
        return
    
    contenuto=str(c)
    larghezza=len(contenuto) + 10
    altezza=5

    for i in range(altezza):
        if i == 0 or i == altezza -1:
            print("*" * larghezza)
        elif i==2:
            print("*"  + " "*4+contenuto+" "*(larghezza-5-len(contenuto)-1)+"*")
        else:
            print("*"+" "* (larghezza-2)+"*")







def main():
    
    alieno = Alieno()
    mostro = Mostro("gOrThOr", "GRAAAHHH", "Uuurghhh")

    print(alieno)
    print("Munizioni:", alieno.getMunizioni())
    print()
    print(mostro)
    print("Assalto:", mostro.getAssalto())
    print()
    print("Combattimento\n")

    vincitore = combattimento(alieno, mostro)

    
    proclamaVincitore(vincitore)



if __name__ == "__main__":
    main()
