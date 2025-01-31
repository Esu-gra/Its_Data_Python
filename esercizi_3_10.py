#esercizi 2-3

'''nome="Gianni"

print(f"Ciao {nome},ti piacerebbe imparare python")'''


#esercizio 2-4

'''nome_maiuscola_minuscola="Gianni"
print(nome_maiuscola_minuscola.upper())
print(nome_maiuscola_minuscola.lower())
print(nome_maiuscola_minuscola.capitalize())'''


#esercizio 2-6


'''Albert_Einstein="Una persona che non ha mai commesso un errore non hai mai provato nulla di nuovo"
print(f"Un giorno Albert_Einstein disse: '{Albert_Einstein}'")'''

#esercizio 3-1
'''
nomi=["Lorenzo","Simone","Giammi","Giorgio"]'''

#pint(nomi[0])

#esercizio2

#print(f"Ciao{nomi[0]}")

#esercizio 3-3
'''mezzi=["Ferrari","Lamborghini","Honda","Polo"]

print(f"Quanto vorrei avere  la {mezzi[1]}")'''

#esercizio 3-4

vip=["Baloteli","Corona","Naingolan"]
'''
print(f"Ciao {vip[1]} , vorrei invitarti a cena domani sera \n fammi sapere , saluti .")

print(f"{vip[2]} non può cucinare ")'''
#esercizio 3-5
'''vip.remove("Naingolan")
print(vip)
vip.append("Messsi")
print(vip)
print(f"Ciao {vip[0]} , vorrei invitarti a cena domani sera \n fammi sapere , saluti .")
print(f"Ciao {vip[1]} , vorrei invitarti a cena domani sera \n fammi sapere , saluti .")
print(f"Ciao {vip[2]} , vorrei invitarti a cena domani sera \n fammi sapere , saluti .")'''

#esercizi 3-6

'''
vip.insert(0,"Simba")
vip.insert(2,"Guè")
print(vip)
print(f"Abbiamo ospiti a cena ragazzi :{vip[0]} e {vip[2]}")
'''

#esercizio 3-7
'''
print("scusate ma devo levare due persone dalla cena :(")
print(f"Mi dispiace {vip[0]}, ma ho dovuto annullare la cena ")
print(f"Mi dispiace {vip[2]}, ma ho dovuto annullare la cena ")
vip.pop(0)
vip.pop(0)
vip.pop(0)
print(vip)
'''
#esercizio 3-8

'''
paesi=["Cancun","London","Barca"]
print(sorted(paesi))
print(paesi)
paesi.reverse()
print(paesi)
'''

#esercizio 3-9

'''
print(len(vip))
'''

#esercizio 3-10

'''
lingue=["Italiano","Spagnolo","Inglese","Francese"]
print(f"Lo {lingue[1]} è più semplice dell'{lingue[2]}")
#print(sorted(lingue))
print(len(vip))
#lingue.reverse()

lingue.append("Mongolo")


lingue.insert(3,"Arabo")


lingue.pop(3)
lingue.remove("Mongolo")
print(lingue)

lingue.extend(["Mongolo","Arabo"])
print(lingue)

del lingue 
print(lingue)
'''