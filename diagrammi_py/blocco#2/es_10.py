
#Validazione dell'età per l'attività


età=int(input("Inserire l'età: "))

if età >= 18 and età <= 65 :
    print("Puoi partecipare all'attività")
else:
    if età < 18:
        print("Non puooi partecipare perchè non hai raggiunto l'età minima")
    else:
        print("non puoi ppartecipare all'attività perche hai superato l'età massima ")