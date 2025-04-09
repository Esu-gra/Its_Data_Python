#7. Algoritmo per il calcolo della media dei voti con inserimento iterativo

cont=0
sum=0

while True:
    scelta=input("Vuoi inserire un voto si/no: ").strip().lower()
    if scelta=="si":
        voto=int(input("inserire voto: "))
        if voto>0:
            cont=cont+1
            sum=sum+voto
        else:
            print("errore")
    else:
        if scelta=="no":
            media=sum/cont
            print(media)
            break