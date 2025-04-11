






#esercizio 6-8
'''
gatto={'nome':"Ernesto",
       'propretario':"Ermanno",
       'età':23
}
cane={'nome':"Ziva",
       'propretario':"Edoardo",
       'età':20
}
criceto={'nome':"Pippo",
       'propretario':"Sofia",
       'età':2
}

animali_domestici={0:gatto,1:cane,2:criceto}
lista_dict=[gatto,cane,criceto]

for c in lista_dict:
        animali_domestici.update(c)
        print(animali_domestici)
        '''
gatto={'nome':"Ernesto",
       'propretario':"Ermanno",
       'età':23
}
cane={'nome':"Ziva",
       'propretario':"Edoardo",
       'età':20
}
criceto={'nome':"Pippo",
       'propretario':"Sofia",
       'età':2
}
lista_dict=[gatto,cane,criceto]

for i in lista_dict:
        print(i)