


def build_cars(prodotto,modello,**kwargs):
    output=f"{prodotto}:{modello},"
    for k,v in kwargs.items():
        output+=f"{k}:{v},"
    print(f"{output}")

build_cars("Ford","Fiesta",color="Red",Posti=None)