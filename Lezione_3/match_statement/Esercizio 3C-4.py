# Scrivere un programma in Python che permetta all'utente
# di inserire il nome di un animale e, utilizzando un match statement,
# identifichi a quale categoria esso appartiene. L'animale deve essere
# classificato in una delle seguenti categorie:


mammiferi=["cane","gatto","cavallo","elefante","leone"]
rettili=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli=["acquila","pappagallo","gufo","falco"]
pesci=[" squalo","trota","salmone","carpa"]

animal=(input("inserire animale: ")).lower()
match animal:
        case _ if animal in mammiferi:
            print("Mammiferi")
        case _ if animal in rettili:
            print("Rettili")
        case _ if animal in uccelli:
            print("Uccelli")
        case _ if animal in pesci :
            print("Pesci")
        case _:
            print("Categoria non conosciuta")