giorno=int(input("giorno: "))
mese=int(input("mese: "))
tup:tuple=(giorno,mese)





match tup:
    case tup if giorno==1 and mese==1:
        print("Capodanno")
    case tup if giorno==14 and mese==2:
        print("S. Valentino")
    case tup if giorno==2 and mese==6:
        print("Festa della R.I")
    case tup if giorno==15 and mese==8:
        print("Ferragosto")
    case tup if giorno==31 and mese==10:
        print("Halloween")
    case tup if giorno==25 and mese==12:
        print("Natale")
    case _:
        print("Nessuna festività importante in questa data.")
    