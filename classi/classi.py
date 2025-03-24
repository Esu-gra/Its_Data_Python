#oggetto istanza di una classe

class persona:
    #costruttore
    def __init__(self,name,eta):
        self.name=name  #attributo di istanza 
        self.eta=eta    #attributo di istanza
        
    #metodo
    def saluta(self):
        return f"ciao mi chiamo {self.name} e ho {self.eta} anni"

#creazione di un oggetto (istanza della classe) 
persona1=persona("esu",23)

#uso di un metodo della classe
print(persona1.saluta())   



class Persona:
    def __init__(self,name,age,uni,new_uni):
        self.name=name
        self.age=age
        self.uni=uni
        self.new_uni=new_uni
    def appello(self):
        return f"Nome: {self.name}, Età: {self.age}, Uni_origin: {self.uni}, New_uni: {self.new_uni}"

student1=Persona("Anna",23,"Roma Tre","Oxford")
print(student1.appello())



class Mammiferi:
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat

    def animale(self):
        return f"Nome animale: {self.name}, Il suo Habitat: {self.habitat}"
    
animal1=Mammiferi("Balena","acqua")

print(animal1.animale())
