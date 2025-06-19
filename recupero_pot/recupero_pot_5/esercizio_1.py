'''
Data una matrice quadrata di dimensione m x m, il carico di una posizione (r,c), indicato con k(r,c), è dato dalla differenza tra la somma degli elementi della riga r e la somma degli elementi della colonna c.
Ad esempio, nella seguente matrice:

1   2   1   1
0   0   0   1
1   1   2   0
2   0   0   0

'''
from random import randint
def mat_quadrata(dim:int) -> list[list[int]]:
    mat:list[int]=[]
    

    
    for _ in range(dim):
        prim = randint(0, 13)
        row = [prim]
        
        while len(row) < dim:
            n = randint(0, 13)
            if n != prim:
                row.append(n)
        mat.append(row)
    return mat





def printMAT(mat: list[list[int]]):
    for row in mat:
        for val in row:
            print(f"{val:<5}", end="")
        print()




def calcolaCarico(mat:list[list[int]],r:int,c:int):
    somma_r=sum(mat[r])
    somma_c=sum((mat[i][c]) for i in range(len(mat)))
        
    return somma_r-somma_c

def caricoNullo(mat:list[list[int]])->list:
    dim=len(mat)
    posizioni=[tuple]
    for r in range(dim):
        for c in range(dim):
            if calcolaCarico(mat,r,c)==0:
                posizioni.append(r)
                posizioni.append(c)
    return posizioni


def caricoMax(mat:list[list[int]])->tuple[int,int]:
    dim=len(mat)
    max_k=None
    max_pos=(0,0)
    for r in range(dim):
        for c in range(dim):
            k=calcolaCarico(mat,r,c)
            if max_k is None or k>max_k:
                max_k=k
                max_pos=(r,c)
    print(f"Carico massimo: {max_k}")
    return max_pos

def caricoMinimo(mat:list[list[int]]):
    dim=len(mat)
    min_k=None
    min_pos=(0,0)
    for r in range(dim):
        for c in range(dim):
            k=calcolaCarico(mat,r,c)
            if min_k is None or k<min_k:
                min_k=k
                min_pos=(r,c)
    print(f"Carico minimo: {min_k}")
    return min_pos






matrice = mat_quadrata(5)
print("Matrice generata:")
printMAT(matrice)

nulle = caricoNullo(matrice)
n_nullo=len(nulle)
print(f"\nPosizioni a carico nullo ({n_nullo}): {nulle}")

rmax, cmax = caricoMax(matrice)
print(f"Indice carico massimo: ({rmax}, {cmax})")
print(f"Verifica carico massimo: k({rmax},{cmax}) = {calcolaCarico(matrice, rmax, cmax)}")

rmin, cmin = caricoMax(matrice)
print(f"Indice carico minimo: ({rmin}, {cmin})")
print(f"Verifica carico minimo: k({rmin},{cmin}) = {calcolaCarico(matrice, rmin, cmin)}")













