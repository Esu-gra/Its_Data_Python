def baricentro(v):
    n = len(v)

    for i in range(n):
       
        somma1 = sum(v[:i+1])
        somma2 = sum(v[i+1:])
        if somma1 == somma2:
            return i
    return None
v=[1,2,3,3,2,1]
print(baricentro(v))


def printResult(v: list[int])->int|None:
    i=baricentro(v)
    if not i== None:
        return f"Esiste un baricentro: {i}"
    else:
        return f"Il baricentro del vettore v={v} non esiste!"

    
print(printResult(v))



def baricentroOttimizzato(v: list[int]):
    n=len(v)
    for i in range(n):
        somma1=sum(v[:i+1])
    for i in range(n):
        somma2=sum(v[i+1:])
    
    if somma1==somma2:
        return f"Baricentro: {i}"
    return None



    


    
   
    
# def baricentro(v):
#     print(f"Controllo il vettore: {v}")
#     n = len(v)
#     for i in range(n):
#         somma1 = sum(v[:i])
#         somma2 = sum(v[i+1:])
#         print(f"Indice {i}: sinistra={somma1}, destra={somma2}")
#         if somma1 == somma2:
#             print(f"Trovato baricentro in i={i}")
#             return i
#     return None


