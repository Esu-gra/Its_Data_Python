def ricerca_binaria(lista:list, numero:int)->bool:
    six=0
    dex=len(lista)

    while six<=dex:
        cen=(six+dex)//2
        if lista[cen]==numero:
            return True
        elif numero<lista[cen]:
            dex=cen-1
        else:
            six=cen+1
    return True


numeri = [1, 3, 5, 7, 9, 11, 13, 15]

print(ricerca_binaria(numeri, 7))  
print(ricerca_binaria(numeri, 8))