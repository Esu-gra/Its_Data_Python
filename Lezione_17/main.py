from dottere import Dottore
from paziente import Paziente
from fattura import Fattura

# Creo i dottori
dottore1 = Dottore("Mario", "Rossi", 45, "Cardiologo", 100.0)
dottore2 = Dottore("Luca", "Bianchi", 50, "Pediatra", 80.0)

# Creo i pazienti
p1 = Paziente("Giulia", "Verdi", 30, "P001")
p2 = Paziente("Marco", "Neri", 40, "P002")
p3 = Paziente("Anna", "Galli", 25, "P003")
p4 = Paziente("Sara", "Russo", 20, "P004")

lista_pazienti1 = [p1, p2, p3]
lista_pazienti2 = [p4]

# Saluto dei dottori
dottore1.doctorGreet()
dottore2.doctorGreet()

# Creo le fatture
fattura1 = Fattura(lista_pazienti1, dottore1)
fattura2 = Fattura(lista_pazienti2, dottore2)

# Stampo i salari
print(f"Salario Dottore1: {fattura1.get_salary()} euro!")
print(f"Salario Dottore2: {fattura2.get_salary()} euro!")

# Rimuovo un paziente dal dottore1 e lo aggiungo a dottore2
fattura2.addPaziente(p2)
fattura1.removePaziente("P002")


# Stampo i nuovi salari
print(f"Salario Dottore1: {fattura1.get_salary()} euro!")
print(f"Salario Dottore2: {fattura2.get_salary()} euro!")

# Guadagno totale
totale = fattura1.get_salary() + fattura2.get_salary()
print(f"In totale, l'ospedale ha incassato: {totale} euro!")
