#esercizio 6-1
'''persona={'Nome':"Giammi",
        'Cognome':"Vatt",
        'Età':34,
        'Città':"Porto"}

print(f"Ciao mi chiamo {persona['Nome']} {persona['Cognome']} ho {persona['Età']} anni e vivo a {persona['Città']}")'''


#esercizio 6-2
'''

numero_fortunato={'Pappa':23,
                  'Tony':8,
                  'Peppe':5,
                  'Lollo':56}
print(numero_fortunato["Pappa"])
'''

#esercizio 6-3

'''
glossario={'.pop()':"Elimina l'elemento selezionato in una lista",
           'len()':"Restituisce il numero totale degli elemnti in una lista ",
           '.reverse()':"Riordina la lista invertendo l'ordine",
           'sorted()':"Ordina la lista in ordine crescente"}

print(f".pop:{glossario['.pop()']} \n .reverse:{glossario['.reverse()']} \n len:{glossario['len()']}\n sorted:{glossario['sorted()']}")
'''


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


#esercizio 6-8
'''
gatto={'nome':"Ernesto",
       'propretario':"Ermanno",
       'età':23
}
cane={'nome':"Ziva",
       'propretario':"Edoardo",
       'età':20
}
criceto={'nome':"Pippo",
       'propretario':"Sofia",
       'età':2
}

animali_domestici={0:gatto,1:cane,2:criceto}
lista_dict=[gatto,cane,criceto]

for c in lista_dict:
        animali_domestici.update(c)
        print(animali_domestici)
        '''
gatto={'nome':"Ernesto",
       'propretario':"Ermanno",
       'età':23
}
cane={'nome':"Ziva",
       'propretario':"Edoardo",
       'età':20
}
criceto={'nome':"Pippo",
       'propretario':"Sofia",
       'età':2
}
lista_dict=[gatto,cane,criceto]

for i in lista_dict:
        print(i)