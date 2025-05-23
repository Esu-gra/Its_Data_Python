'''
Scrivi una funzione che prenda in input una lista
di dizionari che rappresentano voti di studenti e
aggrega i voti per studente in un nuovo dizionario.

'''

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    registro={}
    for studente in voti:
        nome = studente['nome']
        voto = studente['voto']
        
        if nome not in registro:
            registro[nome] = []
        registro[nome].append(voto)

    return registro

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))