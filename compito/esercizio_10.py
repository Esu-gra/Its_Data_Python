# n = int(input("Inserisci un numero: "))
# list_n = []

# while n != 0:
#     list_n.append(n)
#     n = int(input("Inserisci un numero: "))

# somma_pari = 0
# somma_dispari = 0
# conteggio_dispari = 0

# for i in list_n:
#     if i % 2 == 0:
#         somma_pari += i
#     else:
#         somma_dispari += i
#         conteggio_dispari += 1

# media_dispari = somma_dispari / conteggio_dispari if conteggio_dispari > 0 else 0

# frequenza = {}

# for i in list_n:
#     if i in frequenza:
#         frequenza[i] += 1
#     else:
#         frequenza[i] = 1

# frequenza_max = max(frequenza.values(), default=0)
# numeri_frequenti = [k for k, v in frequenza.items() if v == frequenza_max]

# print(f"Somma dei numeri pari: {somma_pari}")
# print(f"Media dei numeri dispari: {media_dispari:.2f}")
# print(f"Numero più frequente: {', '.join(map(str, numeri_frequenti))} ({frequenza_max} volte)")

###############################################################



dict_frequenze={}

while True:
    numero_inserito=int(input("inserire numero: "))

    if numero_inserito in dict_frequenze:
        dict_frequenze[numero_inserito]+=1
    else:
        dict_frequenze[numero_inserito]=1
