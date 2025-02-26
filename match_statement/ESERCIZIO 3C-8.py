frase=input("inserire frase: ")

match frase:
    case frase if frase[-1]=="?" and len(frase)%2==0:
        print("si")
    case frase if frase[-1]=="?" and not(len(frase)%2==0):
        print("No")
    case frase if frase[-1]=="!":
        print("Wow")
    case _:
        print(f"Tu dici: {frase}")