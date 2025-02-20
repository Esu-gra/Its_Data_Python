età=int(input("inserire l'età: "))

if età < 2:
    print("Neonato")
elif età >= 2 and età < 4:
    print("bimbo")
elif età >= 4 and età< 13:
    print("bambino")
elif età >= 13 and età<20:
    print("adolescente")
elif età >= 20 and età < 65:
    print("adulta")
else: 
    print("anziano")


