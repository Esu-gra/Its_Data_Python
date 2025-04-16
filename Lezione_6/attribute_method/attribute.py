# public attribute :
# possiamo sovrascrivere il valore dell'attributo 
# di base è sconsigliato 




# private attribute:

#nessuno ha l'accesso all'attributo tranne la classe che lo tiene ,

#__attribute ---> per modificarlo print(nome:_Class__attribiute)


#oppure si crea un metodo apposta che ritorna :

# return self.__name



# ATTRIBUTI DI CLASSE

# un attributo che fa riferimento alla classe e non alle istanze 
# per accedervi : NomeClasse.attributo_della_classe

#METODO STATICO :

# @staticmethod 
class Math:
    PI : float=3.14

    @staticmethod
    def circle_area(radius:float)->float:
        return Math.PI * radius * radius
    

print(Math.PI)
print(Math.circle_area(4))


#############################

#METODO DI CLASSE  

# @classmethod

# se usiampo classmethod non ci serve il self

# def metodo(cls(che fa riferimento alla clsse)):
       