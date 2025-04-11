# class User:
#     def __init__(self,first_name,last_name,birthday):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.birtday=birthday

    
#     def describe_user(self):
#         print(f"Name: {self.first_name}\nLast Name: {self.last_name}")
    
#     def greetUser(self):
#         print(f"Ciao {self.first_name} come posso aiutarti?")

    


# Anna=User("Anna","Pippa",23)
# Chiara=User("Chiara","Bianchi",12)
# Carlo=User("Carlo","Polpetta",54)

# Anna.describe_user()
# Anna.greetUser()
class Utente:
    def __init__(self,nome,cognome,nome_utente,email):
        self.nome=nome
        self.cognome=cognome
        self.nome_utente=nome_utente
        self.email=email
    def  describe_user(self) :
        return f"Nome: {self.nome}\ncognome:{self.cognome}\nnome_utente:{self.nome_utente}\nemail:{self.email}"


class Privilegi:
    def __init__(self,accesso_full:list):
        self.accesso_full=accesso_full

    
    def show_privileges(self):
        for privilegio in self.accesso_full:
            print(f"-{privilegio}")
        


class Admin:
    def __init__(self, utente: Utente ,privilegio:Privilegi):
        self.utente=utente
        self.privilegio=privilegio