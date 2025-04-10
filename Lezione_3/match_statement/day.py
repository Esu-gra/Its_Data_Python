#Chiedere all'utente di inserire un numero da 1 a 7 che rappresenta un giorno 
# della settimana e stampare il nome del giorno corrispondente.


day=int(input("Inserire un numero da 1 a 7 del gioro della settimana: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("sunday")

