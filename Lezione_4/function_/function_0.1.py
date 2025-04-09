
# for i in range(1,11):
   
#     sum=sum+i
# print(sum)


# for i in range(20,38):
#     sum=sum+i
# print(sum)


# for i in range(35,50):
#     sum=sum+i
# print(sum)



# Usiamo la funzione per poter evitare ripetizione di codice (concetto di riutilizzo del codice)


# the syntax :


#  def -->parola chiave
#def nome_funzione():

#due tipi di funzioni  ----> funzione che richiede un valore in input

                             #funzione che non richiede un valore in input


def sum_function(x:int,y:int):
    sum=0
    for i in range(x,y+1):
        sum=sum+i
   

    return sum

print(sum_function(35,50))
print(sum_function(20,38))
my_sum=sum_function(1,10)
print(my_sum)


#possiamo definire una funzione come un gruppo
#di istruzione che svolgono un operazione specifica

def subtract(a,b):
    sottra=a-b
    
    return sottra

print(subtract(12,34))


print(type(subtract(23,5))) #-------> ci stampa il tipo di dato



#queste funzioni create da noi vengono definite 'user-defined'

# 'return'-------> rsetituisce un valore definita nella funzione 




#esempio

def età_function():
    età=int(input("inserire età: "))
    if età<=18:
        print("non puoi entrare ")
    else:
        print("Puoi entrare")

età_function()