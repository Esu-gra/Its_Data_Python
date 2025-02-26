while True:
    parola=input("inserire parola: ").strip().lower()
    if parola[0]==parola[-1]:
        print("caratteri uguali")
    
    if parola=="fine":
        break
    else:
        continue



