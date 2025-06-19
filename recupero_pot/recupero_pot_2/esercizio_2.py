
def printListBackward(lista):
    if not lista:
        return
    printListBackward(lista[1:])  
    print(lista[0])               


liste_di_test = [
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c'],
    [],
    [100],
    [10, 20, 30, 40]
]

for i, l in enumerate(liste_di_test, start=1):
    print(f"Lista {i} stampata al contrario:")
    printListBackward(l)
    print('-' * 30)

list1=[1, 2, 3, 4, 5]
list2=["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]