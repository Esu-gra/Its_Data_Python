class User:
    def __init__(self,first_name,last_name,birthday,login_attempts=0):
        
        self.first_name=first_name
        self.last_name=last_name
        self.birtday=birthday
        self.login_attempts=login_attempts

    
    def describe_user(self):
        print(f"Name: {self.first_name}\nLast Name: {self.last_name}")
    
    def greetUser(self):
        print(f"Ciao {self.first_name} come posso aiutarti?")
    
    def increment_login_attepts(self):
        self.login_attempts+=1
    def reset_login_attepts(self):
        self.login_attempts=0

        
    def display_login_attempts(self):
        print(f"tentativi di accesso: {self.login_attempts}")
        
    
    
        
    

     

    


Anna=User("Anna","Pippa",23)
Chiara=User("Chiara","Bianchi",12)
Carlo=User("Carlo","Polpetta",54)

Anna.describe_user()


Anna.increment_login_attepts()
Anna.increment_login_attepts()

Anna.display_login_attempts()

Anna.reset_login_attepts()
Anna.display_login_attempts()