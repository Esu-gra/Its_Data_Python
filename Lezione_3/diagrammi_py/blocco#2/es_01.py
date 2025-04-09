'''
Sistema di gestione per un parcheggio
Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio con un numero massimo di posti dato in input. L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:

se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
se l'utente inserisce "esci", termina l'algoritmo.
Torna all'inserimento di una opzione finché l'utente non seleziona "esci".
'''

max_posti=int(input("Inserire numero massimo del parcheggio: "))
liberi=max_posti
while True:
    opzione=input("scegliere opzione: 'ingresso','uscita','stato','esci': ").strip().lower()
    if opzione=="ingresso":
        if liberi > 0:
            liberi=liberi-1
        else:
            print("non ci sono posti")
    elif opzione=="uscita":
        if liberi <max_posti:
            liberi=liberi+1
        else:
            print("tutti i posti sono già occupati")
    elif opzione=="stato":
        print(liberi)
        print(max_posti-liberi)
    elif opzione=="esci":
        break
    else:
        continue
