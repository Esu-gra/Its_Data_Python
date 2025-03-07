def make_album(name:str,title:str,n_brani:int):
    return {f"name:{name}, title:{title}, numero_brani:{n_brani}"}



while True:
    album=input("Inserire titolo: ")
    artista=input("Inserire artista: ")
    print(make_album(f"{album}",f"{artista}" ,f"{None}"))
