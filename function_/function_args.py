


def addition(a,b):
    return a+b
print(addition(12,4))
#print(addition(12,4,5)) #errore perche c'è un parametro di troppo

################################


my_list=[1,2,3,4,5]
print(my_list)
print(*my_list) #------> ci permette di stampare gli elementi senza le perentesi


#####################################

#  ARGS --------> creare una funzione che ammette un infinito di parametri

def add(*args):
    tot=0
    for numbers in args:
        tot+=numbers
    return tot

print(add(12,6,23))
 

# KWARGS  ---------> con chiave e valore 

def total_pirce(**kwargs):
    total:float=0
    for product,price in kwargs.items():
        print(f"{product} : {price}")
        total+=price
    return round(total,2)
print(f"total: {total_pirce(coffi=2.34,latte=1.45)}")


