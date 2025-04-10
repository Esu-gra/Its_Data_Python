
mammiferi=["cane","gatto","cavallo","elefante","leone"]
rettili=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli=["acquila","pappagallo","gufo","falco"]
pesci=["squalo","trota","salmone","carpa"]

habitat_t=["acqua","aria","terra"]

     


animal=(input("inserire animale: ")).lower()
habitat=input("inserire habitat: acqua,aria,terra: ").strip().lower()

match animal:
        case animal if animal in mammiferi:
            print("Mammiferi")
        case animal if animal in rettili:
            print("Rettili")
        case animal if animal in uccelli:
            print("Uccelli")
        case animal if animal in pesci :
            print("Pesci")
        case _:
            print("Categoria non conosciuta")

# match animal:
#         case _ if animal in mammiferi and habitat==habitat_t[2]:
#             print("Categoria: Mammiferi")
#             print(f"{animal} è uno degli animali che vive sulla terra")
    
#         case _ if animal in rettili :
#             print("Categoria: Rettili")
#         case _ if animal=="coccodrillo":
#             print(f"Il {animal} vive sia in terra che in acqua")


#         case _ if animal in uccelli and  habitat==habitat_t[1]:
#             print("Categoria: Uccelli")
#             print(f"{animal} il suo ahabitat è l'aria")

            
#         case _ if animal in pesci and habitat==habitat_t[0]:
#             print("Categoria: Pesci")
#             print(f"{animal} il suo habitat è l'acqua")
#         case _:
#             print("Categoria non conosciuta")

