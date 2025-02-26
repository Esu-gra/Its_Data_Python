
# i=0
# somma=0
# media=0
# n_grande=0
# n_piccolo=0


# while True:
#     n=float(input("inserire numero: "))
#     if n > 0:
#         i=1
#         somma=n
#         media=somma/i
#         n_grande=0
#         n_piccolo=0
#         if n.is_integer():
#           i+=1
#           somma=somma+n
#           media=media+(somma/i)
      
#         else:
#            continue
#         if n < n_grande:
#            n=n_grande
#         if n > n_piccolo:
#            n_piccolo=n
#     else:
#         break
# print(f"media: {media} , numero più grande: {n_grande} , numero più piccolo: {n_piccolo}")
      

i = 0
somma = 0
media = 0
n_grande = None  
n_piccolo = None

while True:
    n = float(input("Inserire numero (negativo per terminare): "))

    if n < 0:
        break  

    i += 1 
    somma += n  

    if n_grande is None or n > n_grande:
        n_grande = n  
    if n_piccolo is None or n < n_piccolo:
        n_piccolo = n 
if i > 0:
    media = somma / i
else:
    media = 0
    n_grande = "non disponibile"
    n_piccolo = "non disponibile"

print(f"Media: {media}, Numero più grande: {n_grande}, Numero più piccolo: {n_piccolo}")

     