'''
Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:
1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).
2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).

'''
def sum_primary_diagonal(matrix)->int:
    x = 0  
    i = 0 

    for riga in matrix:
        x += riga[i]
        i += 1

    return x

mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(sum_primary_diagonal(mat1))

def sum_secondary_diagonal(matrix)->int:
    x = 0  
    i = 0  
    n = len(matrix)

    for riga in matrix:
        x += riga[n - 1 - i]  
        i += 1

    return x




print(sum_secondary_diagonal(mat1))



def primary_diag(m:list[list[int]])->int:
    somma:int=0
    somma_2:int=0

    for i in range(len(m)):
        somma+=m[i][i]
        somma_2+=m[i][len(m)-1-i]
    return somma

print(primary_diag(mat1))