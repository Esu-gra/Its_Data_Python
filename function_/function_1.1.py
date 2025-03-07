
#tre tipi  per passare i parametri alla fonzuione: 



#--- by position

# def get_user(myName,Role):
#     return {"nome":myName,"role":Role}
# user=get_user("Aldo","Admin")
########################################



#---by keyword

def get_user(myName,Role):
    return {"nome":myName,"role":Role}
user=get_user("Aldo","Admin")
print(get_user(myName="Esu",Role="Admin"))




def describe_person(name,age:int,city):
    print(f"Ciao sono {name} ho {age} e vivo a {city}")
describe_person(name="Esu",age=21,city="Roma")

############################################


#----by default value 

def totale(x,y,w=12,c=3):
    x=w
    y=c
    return(x**y) + w+c

print(totale(12,2))
print(totale(12,2,8))#----------
                               #|
                               #|  

print(totale(12,4,6,9))#-------> possiamo cambiare i paramentri anche se sono stati gia inseriti 


