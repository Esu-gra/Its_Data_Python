# cronometro

def cronometro(fun):
    def wrapper(*args): # decorator con input in ingresso o anche no 
        import time
        start=time.time()
        fun(*args)
        print(time.time()-start)
    return wrapper

@cronometro
def prova():
    for i in range(100000):
        pass

# equivale a scrivere @cronometro definito decoratore
prov=cronometro(prova)


prova()


