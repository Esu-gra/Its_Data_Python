# def build_profilo(**kwargs):
#     for k,val in kwargs.items():
#         print(f"name:{k}:{val}", f"età:{k}:{val}",f"{k}:{val}")
    


def build_profile(first_name:str,last_name:str,**kwargs)->str:
    output=f"{first_name} {last_name},"    
    for k,v in kwargs.items():
        output+=f"{k} {v},"
    print({output})


build_profile("Alessio","Natale",age=23,hair="Black",weight=67,height=120)