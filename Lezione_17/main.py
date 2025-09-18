from dottere import Dottore
from fattura import Fattura
from paziente import Paziente

# Creo pazienti
p1 = Paziente("Lorenzo", "Pola", "c1")
p2 = Paziente("Edo", "Saola", "c2")
p3 = Paziente("Ciccio", "Palla", "c3")
p4 = Paziente("Pippo", "Tanto", "c4")

l1 = [p2, p3, p4]
l2 = [p1]

# Creo dottori (attenzione all'ordine: nome, cognome, età, parcella, specializzazione)
d1 = Dottore("Giggi", "Poldo", 40, 340.0, "Chirurgo")
d2 = Dottore("Nino", "D'Angelo", 45, 250.0, "Pediatra")

# Saluto dei dottori
print(d1.doctorGreet())
print(d2.doctorGreet())

# Creo fatture
fattura1 = Fattura(l1, d1)
fattura2 = Fattura(l2, d2)

print(f"Salario Dottore1: {fattura1.get_salary()} euro!")
print(f"Salario Dottore2: {fattura2.get_salary()} euro!")

# Rimuovo un paziente da dottore 1 e lo aggiungo a dottore 2
p_to_move = l1.pop(0)  # tolgo il primo paziente da l1
l2.append(p_to_move)

# Aggiorno fatture
fattura1 = Fattura(l1, d1)
fattura2 = Fattura(l2, d2)

print(f"Salario Dottore1: {fattura1.get_salary()} euro!")
print(f"Salario Dottore2: {fattura2.get_salary()} euro!")

# Guadagno totale
totale = fattura1.get_salary() + fattura2.get_salary()
print(f"In totale, l'ospedale ha incassato: {totale} euro!")
