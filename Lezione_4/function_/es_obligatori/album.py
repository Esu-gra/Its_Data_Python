def make_album(name:str,title:str,n_brani:int):
    return {f"name:{name}, title:{title}, numero_brani:{n_brani}"}
    
print(make_album("Lazza","Remida",None))
print(make_album("Sfera","Rockstar",22))
print(make_album("Gue","Gentleman",34))