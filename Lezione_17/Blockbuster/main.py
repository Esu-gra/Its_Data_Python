from movie_genre import *
from film import *
from noleggio import *


f1=Dramma(1,"La maga")

f2=Azione(2,"Balla")
f3=Azione(23,"Gallo")
f4=Azione(12,"Giggio")
f5=Azione(62,"Mamma ho perso")
f6=Azione(92,"Mammandnoed")


f7=Commedia(34,"Natale a Roma")
f8=Commedia(4,"Nonno scatento")
f9=Commedia(78,"Ha Paura")
f10=Commedia(344,"Herry Fottter")

film_list=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
n=Noleggio(film_list)

print("Quale film vuoi noleggaiare ?")
n.isAvaible(f4)
n.isAvaible(f6)
n2=Noleggio(film_list)

n2.isAvaible(f6)
n2.isAvaible(f9)

n.givBack(f6,n,2)

print(n._film_list)