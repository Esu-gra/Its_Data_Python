class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def presentazione(self):
        return f"Nome:{self.name},Età: {self.age}"



alice=Person("Alice",23)
gionni=Person("Gionni",34)
edo=Person("Edo",23)
lollo=Person("Lollo",12)
piero=Person("Pier",45)
# print(alice.presentazione())
# print(gionni.presentazione())
people=[alice,gionni,edo,lollo,piero]
minimo=float("inf")

for i in people:
    if i.age<minimo:
        minimo=i.age
        name=i.name
print(name)
    

# if alice.age > gionni.age:
#     print(alice.presentazione())
# else:
#     print(gionni.presentazione())

