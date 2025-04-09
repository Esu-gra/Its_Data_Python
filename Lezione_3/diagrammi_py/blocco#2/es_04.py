'''
. Assegnazione di un tutor
Progettare un algoritmo che assegni i 10 tutor disponibili
agli studenti che necessitano di recupero in un istituto scolastico.
Per ogni studente dato in input, il sistema deve controllare la 
disponibilità dei tutor e, nel caso di disponibilità, assegnarlo allo studente. Se il numero di tutor disponibili scende a zero, occorre aumentare il numero di studenti in lista d'attesa.
Occorre confermare sia l’assegnazione del tutor con successo che
l'inserimento nella lista d’attesa allo studente. L'algoritmo termina solo quando il numero di tutor è pari a 0 e la lista d'attesa conta 50 studenti.
'''


n_tutor=10
attesa=0

while True:
    studente=input("richiesta docente?>").strip().lower()
    if n_tutor>0:
        n_tutor=n_tutor-1
        print("Tutor assegnato")
    else:
        attesa=attesa+1
        print("Studente in attesa")
    if n_tutor==0 and attesa>5:
        break
    else:
        studente
