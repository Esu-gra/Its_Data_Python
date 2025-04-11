#esercizio 5-5
alien_color=input("inserire colore: ").strip().lower()


if alien_color=="verde":
    print("il giocatore ha  guadagnato 5 unti.")
elif alien_color=="giallo":
    print("il giocatore ha guadagnato 10 punti.")
else:
    print(" il giocatore ha guadagnato 15 punti.")