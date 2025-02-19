pizza=["Margherita","Americana","4 formaggi"]



friend_pizzas=list(pizza)
  
pizza.append("Fiori")
pizza.insert(2,"Diavola")
#print(pizza)


friend_pizzas.append("Norcina")
friend_pizzas.insert(3,"Patatosa")
#print(friend_pizzas)


print("Le mie pizze preferitebsono sono:")

for i in pizza:
    print(i)


print("Le pizze preferite del mio amico sono: ")
for y in friend_pizzas:
    print(y)