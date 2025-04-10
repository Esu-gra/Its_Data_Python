def validete_password(password):
    errors=[]

    if len(password)<20:
        errors.append("La password deve contenere almeno 20 caretteri")

    uppercase_count=sum(1 for c in password if c.isupper())

    if uppercase_count<3:
        errors.append("la password deve contenere almeno 3 lettere maiuscole")
    
    special_count= sum(1 for c in password if not c.isalnum())
    if special_count<4:
        errors.append("la password deve contenere almeno 4 caratteri speciali")

    
    if errors:
        raise ValueError("Password non valida:\n " + "\n".join(errors))
    
    return True



try:
    validete_password("Bb!cD@eF#gHiJkL12345")
    print("Password valida ")
except ValueError as error:
    print(error)
         

