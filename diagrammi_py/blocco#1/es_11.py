liberi=20

while True:
    opzioni=input("inserire l'opzione desiderata: 'prenota','libera','visualizza','esci': ")
    if opzioni=="prenota":
        if liberi>0:
            liberi-=1
        else:
            print("non ci sono posti disponibili")
    elif opzioni=="libera":
        if liberi<20:
            liberi+=1
        else:
            print("tutti i posti sono già disponibili")
    elif opzioni=="visualizza":
        print(liberi)
        print(20-liberi)
    else:
        if opzioni=="esci":
            break
        else:
            continue
      
        
