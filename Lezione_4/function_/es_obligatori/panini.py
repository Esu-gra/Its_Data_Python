def panini_function(*args):
    panino:str=[]
    for i in args:
        panino.append(i)
    print("panino con: ", *panino) 
        

panini_function("Humburger","Cheddar","Bacon")