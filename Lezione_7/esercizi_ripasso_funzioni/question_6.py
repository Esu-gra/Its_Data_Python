'''
PARTE 1

Scrivi una funzione chiamata create_contact() 
che accetta il nome e cognome, e-mail (facoltativo)
e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
'''

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
   registro = {
        'profile': name,
        'email': email,
        'telefono': telefono
    }


   return registro



def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if dictionary["profile"] == name :
        if email is not None:
            dictionary["email"] = email
        if telefono is not None:
            dictionary["telefono"] = telefono
        else:
            telefono=None
        
    return dictionary
               

# contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
# print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
# print(update_contact(contact, "Mario Rossi", telefono=123456789))


contact2 = create_contact("Laura Neri", email="laura.neri@domain.com")
print(create_contact("Laura Neri", email="laura.neri@domain.com"))
print(update_contact(contact2, "Laura Neri", email="laura.new@domain.com", telefono=84736736))