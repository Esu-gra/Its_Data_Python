def validete_password(password):
    try:
        len(password)>=20
    except ValueError as Errore:
        print("La lunghezza deve essere almeno di 20 caratteri")

    try:
        for i in password:
            maiuscole=i.isupper()
            if maiuscole>3:
                pass
    except ValueError as Error:
        print("Almeno tre lettere devono essere maiuscole")
    try:


         
           