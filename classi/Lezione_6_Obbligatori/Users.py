class User:
    def __init__(self,first_name,last_name,birthday):
        self.first_name=first_name
        self.last_name=last_name
        self.birtday=birthday

    
    def describe_user(self):
        print(f"Name: {self.first_name}\nLast Name: {self.last_name}")
    
    def greetUser(self):
        print(f"Ciao {self.first_name} come posso aiutarti?")

    


Anna=User("Anna","Pippa",23)
Chiara=User("Chiara","Bianchi",12)
Carlo=User("Carlo","Polpetta",54)

Anna.describe_user()
Anna.greetUser()