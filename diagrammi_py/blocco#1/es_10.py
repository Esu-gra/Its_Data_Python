reddito=int(input("inserire il suo reddito: "))
media=int(input("inserire la sua media: "))

if reddito<20000 and media>27:
    print("Borsa di studio approvata")
else: 
    print("Borsa di studio rifiutata.(Motivo: reddito o media insufficente)")

    