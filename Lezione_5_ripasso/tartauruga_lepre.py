import random

LUNGHEZZA_PERCORSO = 70
CAMBIO_METEO_E_OGNI = 10
ENERGIA_MAX = 100
OSTACOLI = {15: -3, 30: -5, 45: -7}
BONUS = {10: 5, 25: 3, 50: 10}


#stato iniziale
pos_tarta = 1
pos_lepre = 1
energia_tarta = ENERGIA_MAX
energia_lepre = ENERGIA_MAX
tempo = 0
meteo = "soleggiato"

# funzione per la pista
def mostra_pista(tarta, lepre):
    pista = ['_'] * LUNGHEZZA_PERCORSO
    if tarta == lepre:
        pista[tarta - 1] = 'OUCH!!!'
    else:
        pista[tarta - 1] = 'T'
        pista[lepre - 1] = 'H'
    print(''.join(pista))

# funzione  meteo
def cambia_meteo():
    return random.choice(["soleggiato", "pioggia"])

# Funzione per muovere la tartaruga
def muovi_tarta(pos, energia, meteo_attuale):
    tiro = random.randint(1, 10)
    penalita = -1 if meteo_attuale == "pioggia" else 0

    if 1 <= tiro <= 5:
        if energia >= 5:
            pos += 3 + penalita
            energia -= 5
        else:
            energia = min(energia + 10, ENERGIA_MAX)
    elif 6 <= tiro <= 7:
        if energia >= 10:
            pos -= 6 - penalita
            pos = max(1, pos)
            energia -= 10
        else:
            energia = min(energia + 10, ENERGIA_MAX)
    elif 8 <= tiro <= 10:
        if energia >= 3:
            pos += 1 + penalita
            energia -= 3
        else:
            energia = min(energia + 10, ENERGIA_MAX)

    # Effetti ostacoli e bonus
    if pos in OSTACOLI:
        pos += OSTACOLI[pos]
        pos = max(1, pos)
    if pos in BONUS:
        pos += BONUS[pos]
        pos = min(pos, LUNGHEZZA_PERCORSO)

    return pos, energia

# Funzione per muovere la lepre
def muovi_lepre(pos, energia, meteo_attuale):
    tiro = random.randint(1, 10)
    penalita = -2 if meteo_attuale == "pioggia" else 0

    if 1 <= tiro <= 2:
        energia = min(energia + 10, ENERGIA_MAX)
    elif 3 <= tiro <= 4:
        if energia >= 15:
            pos += 9 + penalita
            energia -= 15
        else:
            energia = min(energia + 10, ENERGIA_MAX)
    elif tiro == 5:
        if energia >= 20:
            pos -= 12 - penalita
            pos = max(1, pos)
            energia -= 20
        else:
            energia = min(energia + 10, ENERGIA_MAX)
    elif 6 <= tiro <= 8:
        if energia >= 5:
            pos += 1 + penalita
            energia -= 5
        else:
            energia = min(energia + 10, ENERGIA_MAX)
    elif 9 <= tiro <= 10:
        if energia >= 8:
            pos -= 2 - penalita
            pos = max(1, pos)
            energia -= 8
        else:
            energia = min(energia + 10, ENERGIA_MAX)

    # Effetti ostacoli e bonus
    if pos in OSTACOLI:
        pos += OSTACOLI[pos]
        pos = max(1, pos)
    if pos in BONUS:
        pos += BONUS[pos]
        pos = min(pos, LUNGHEZZA_PERCORSO)

    return pos, energia

# Inizio gara
print("BANG !!!!! AND THEY'RE OFF !!!!!")

while pos_tarta < LUNGHEZZA_PERCORSO and pos_lepre < LUNGHEZZA_PERCORSO:
    if tempo % CAMBIO_METEO_E_OGNI == 0:
        meteo = cambia_meteo()
        print(f"Meteo: {meteo}")

    # Muovi tartaruga e lepre
    pos_tarta, energia_tarta = muovi_tarta(pos_tarta, energia_tarta, meteo)
    pos_lepre, energia_lepre = muovi_lepre(pos_lepre, energia_lepre, meteo)

    # Mostra la corsia
    mostra_pista(pos_tarta, pos_lepre)

    # Controlla vittoria
    if pos_tarta >= LUNGHEZZA_PERCORSO and pos_lepre >= LUNGHEZZA_PERCORSO:
        print("IT'S A TIE.")
        break
    elif pos_tarta >= LUNGHEZZA_PERCORSO:
        print("TORTOISE WINS! || VAY!!!")
        break
    elif pos_lepre >= LUNGHEZZA_PERCORSO:
        print("HARE WINS || YUCH!!!")
        break

    tempo += 1
