import random

pos_tartaruga=1
pos_lepre=1
energia_tartaruga=100
energia_lepre=100
sole=0
pioggia=0
tick=+1
count=1

corsia_di_gara=[]
start="BANG !!! AND THEY'RE OF !!!!"


#funzione per visualizzare le posizioni sulla corsia di gara
#funzione per calcolare la mossa della tartaruga
#funzione per calcolare la mossa della lepre 

def posizione_corsia():
    corsia_di_gara = ["-" for _ in range(71)] 
    for i in range(71):
        i=="_"
    print(" ".join(corsia_di_gara))


def mossa_tartaruga():
    tick = random.randint(0, 1)  
    
    if tick == 1:
        pos_tartaruga = 1
    else:
        pos_tartaruga = random.randint(1, 50) 

    return pos_tartaruga  

print(mossa_tartaruga())
        


def mossa_lepre():
    tick = random.randint(0, 1)  
    
    if tick == 1:
        pos_lepre = 1
    else:
        pos_lepre = random.randint(1, 50)  

    return pos_lepre

print(mossa_lepre())




#loop per simulare il tick , calcolare la mossa , mostrare la posizione sulla cprsia di gara,e determinare l'eventuale fine della gara


    



    
