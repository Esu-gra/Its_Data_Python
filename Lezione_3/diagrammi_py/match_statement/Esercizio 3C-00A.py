#Scrivere un programma in Python che richieda all'utente di 
# inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:


bimbo=int(input("Inserire età: "))


match bimbo:
    case 1:
        print("Congratulazione")
    case 2:
        print("Wow! gemelli")
    case 3:
        print("Wow! tre")
    case 4:
        print("Mamma mia Quattro! Wow!")
    case 5:
        print("Incredibile!Cincque!")
    case _:
        print(f"Non ci credo! {bimbo} bambini")


