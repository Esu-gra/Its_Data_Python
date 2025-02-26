x=int(input("Asse x: "))
y=int(input("Asse y: "))
tup:tuple=(x,y)


match tup:
    case tup if x==0 and y==0:
        print("Il punto si trova nell'origine.")
    case tup if y==0:
        print( "Il punto si trova sull'asse X.")
    case tup if x==0:
        print("Il punto si trova sull'asse Y.")
    case tup if x > 0 and y>0:
        print("Il punto si trova nel primo quadrante")
    case tup if x<0 and y>0:
        print("Il punto si trova nel secondo quadrante.")
    case tup if x<0 and y<0:
        print("Il punto si trova nel terzo quadrante.")
    case tup if x>0 and y<0:
        print("Il punto si trova nel quarto quadrante.")
    
