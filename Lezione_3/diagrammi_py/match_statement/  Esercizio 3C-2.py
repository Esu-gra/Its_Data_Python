#Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) 
# nel sistema GPA americano (scala 0-4).
#Il programma deve accettare in input un voto di laurea compreso tra 66 e 110,
#  espresso come numero intero e usare un match per determinare il corrispondente
#  GPA americano, secondo questa tabella di conversione:

voto=int(input("inserire voto: "))

match voto:
    case voto if voto>=106 or voto==110:
        print("GPA: 4.0")
    case voto if voto>=101 or voto==105:
        print("GPA: 3.7")
    case voto if voto>=96 or voto==100:
        print("GPA: 3.3")
    case voto if voto>=91 or voto==95:
        print("GPA: 3.0")
    case voto if voto>=86 or voto==90:
        print("GPA: 2.7")
    case voto if voto>=81 or voto==85:
        print("GPA: 2.3")
    case voto if voto >=76 or voto==80:
        print("GPA: 2.0 ")
    case voto if voto>=70 or voto==75:
        print("GPA: 1.7")
    case voto if voto>=66 or voto==69:
        print("GPA: 1.0")
    case _:
        print("Voto non valido")