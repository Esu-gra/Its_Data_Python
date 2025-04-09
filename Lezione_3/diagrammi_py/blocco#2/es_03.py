
max_posti=10

while True:
    opzione=input("scegli l'opzione:'iscrivi', 'annulla','visualizza','elimina','esci'  ").strip().lower()
    if opzione=="iscrivi":
        if max_posti>0:
            max_posti=max_posti-1
        else:
            print("Non ci sono posti disponibili")
    elif opzione=="annulla":
        if max_posti<10:
            max_posti=max_posti+1
        else:
            print("Tutti i posti sono disponibili")
    elif opzione=="visualizza":
        print(max_posti)
        print(10-max_posti)
    elif opzione=="elimina":
        max_posti=max_posti+1
        10+max_posti
        
    elif  opzione=="esci":
          break
    else:
        opzione