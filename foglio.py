'''
lista=[2,3,4,5]


x=lista.pop(3) #--------------> elimina l'elemento e lo salva nella variabile 
print(x)

lista.remove(4) #------------> elimina l'elemnto senza la possibilità di salvarlo
print(lista)

del lista #----------> elimina la lista 
'''




'''

# vip=["Balotelli","Corona","Naingolan","D.T.","musk"]


# escluso=vip.pop(0)
# print(f"Mi dispiace {escluso} sei fuori!")
'''





'''

lista=[2,3,4,5,45,12,34,56,67]

for i in range(len(lista)):
    x=lista[i]
    print(f"sto rimuovendo {x}")



for i in range(len(lista)-1,-1,-1):
    
    print(f"sto rimuovendo l'elemnto all'indice {i}")
    lista.remove(lista[i])



pop()

while len(lista) >0 :
    x=lista.pop()
    print(f"Ho eliminato {x}")



sorted()   sort()  -----------> riordinare una lista 

sorted(lista,reverse=True,key=lambda x: x**2)
print(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)


list=lista.copy()

print(list)

list.append("g")
print(list)
print(lista)
'''

#update 


dict={"y":9,"c":8}

# s=()

# s.update(dict)
# print(s)





for c in dict.items():
    print(c)


for v,u in dict.items():
    print(v,u)





#impacchetare e spacchettatura



'''

tup=(34,78,67,9)


x,y,c,y=tup


print(x)
print(c)
'''


#################################################

l=[12,34]
# l.extend(dict)
# print(l)

# l2=[34,5,6]
# print(l+l2)
# print(l*2)

##################################################



#moltiplicare gli elemnti di una lista 

def molt_lista(l: list,n:float)-> list:
    '''
    restituisce una lista con gli elementi moltiplicati l=[[]*2]
    '''
    l1=[]
    for el in l:
         l1+=[el*n]#l1.append(el*n)
    return l1
print(molt_lista(l,2))

#####################################################


