

n= int(input("inserire euro: "))


barretta = n 
buoni = barretta
totale_barrette = barretta

while buoni_sconto >= 6:
    barrette_gratuite = buoni_sconto // 6
    print(barrette_gratuite)
    totale_barrette += barrette_gratuite  
    buoni_sconto = buoni_sconto % 6 + barrette_gratuite  


print(f"Totale barrette ottenute: {totale_barrette}")
print(f"Buoni sconto avanzati: {buoni_sconto}")