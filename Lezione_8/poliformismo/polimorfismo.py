from persona import Persona
from alieno import Alieno


#creare oggetto p della classe persona 

p:Persona=Persona("Esu","Grappa",22)

#visualizzare le info relative a p 

print(p)



#oggetto et oggetto alieno 

et:Alieno=Alieno("Andromeda")

print(et)


#oggetto p invoca il  metodo speak()
p.speak()

#oggetto et invoca metodo speak()
et.speak()