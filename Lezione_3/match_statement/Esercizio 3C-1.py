#Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
#Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:


voto=int(input("inserire un voto da 1 a 10: "))

match voto:
    case voto if voto==10:
        print("Eccellente")
    case voto if voto==8 or voto==9:
        print("Molto buono")
    case voto if voto==6 or voto==7:
        print("Sufficiente") 
    case voto if voto==4 or voto==5:
        print("Insufficente")
    case voto if voto>=1 or voto==3:
        print("Gravemente insufficente")
    case _:
        print("Voto non valido")
