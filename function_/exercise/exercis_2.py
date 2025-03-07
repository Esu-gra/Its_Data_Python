def check_length(b=str):
    if len(b)>10:
        print(f"la lunghezza dii {b} è maggiore di 10")
    elif len(b)<10:
        print(f"la lunghezza di {b} è più piccolo di 10")
    else:
        print(f"la lunghezza di {b} è uguale a 10")
    

check_length("ciaooooouii")