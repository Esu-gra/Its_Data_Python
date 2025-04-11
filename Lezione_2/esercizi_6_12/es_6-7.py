#esercizio 6-7
'''
persona={'Nome':"Giammi",
        'Cognome':"Vatt",
        'Età':34,
        'Città':"Porto"}

persona_1_2={'Nome':"Leo",
             'Cognome':"Pappa",
             'Età':56,
             'Città':"Roma"}

persona_1_3={'Nome':"Lollo",
             'Cognome':"Mazza",
             'Età':89,
             'Città':"Catanzaro"}

persone={0: persona, 1: persona_1_2, 2: persona_1_3 }

list_dict = [persona, persona_1_2, persona_1_3]
for d in list_dict:
    persone.update(d)
    print(f"{persone=}")
    
print(persone)
'''

