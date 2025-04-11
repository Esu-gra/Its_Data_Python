# # dal fil persona.py importa la classe Persona
# from persona import Persona

# # creare un oggetto di persona 

# e_g=Persona("Esu","Grappa",22)
# print(e_g)

# print(e_g.name,e_g.cognome,e_g.età)



from persona2 import Persona

eg=Persona()
eg.disply_Data()

#impostare il nome della persona 
print("----------------")

eg.setNome("Esu")
eg.disply_Data()

print("----------------")

eg.setCognome("Grappa")
eg.disply_Data()

print("----------------")

eg.setEtà(12)
eg.disply_Data()

print("----------------")

print(eg.getName(),eg.getCognome(),eg.getEtà())