#Scrivere un programma in Python che memorizzi il nome, 
#il ruolo e l'età di un utente in un dizionario. Il nome,
# il ruolo e l'età devono essere inseriti in input dall'utente 
# stesso. Il programma deve determinare il livello di accesso 
# ai servizi in base al ruolo e all'età dell'utente secondo questo schema:


nome =input("nome: ").strip().lower
ruolo=input("ruolo: ").strip().lower()
età=int(input("età: "))

utenti={"nome":nome,
        "ruolo":ruolo,
        "età":età
}


match utenti:
    case utenti if ruolo=="admin":
        print("Accesso completo a tutte le funzionalità")
    case utenti if ruolo=="moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case utenti if età >=18:
        print("Accesso standard a tutti i servizi.")
    case utenti if ruolo=="ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print( "Attenzione! Ruolo non riconsciuto! Accesso Negato!")