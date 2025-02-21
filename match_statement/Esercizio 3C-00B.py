#Scrivere un programma in Python che chieda all'utente di inserire
# il proprio nome e il proprio genere (specificato con "m" per maschio 
# o "f" per femmina) e utilizzi lo statement match per fornire una risposta adeguata 
# da inserire in un documento di identita'.


name=input("Inserire nome: ")
gender=input("m/f: ").strip().lower()

match gender:
    case "f":
        print(f"Nome: {name} ,genere: Femmina")
    case "m":
        print(f"Nome: {name}  ,genere: Maschio")
    case _:
        print("non è possibile generare un documento di identità.")