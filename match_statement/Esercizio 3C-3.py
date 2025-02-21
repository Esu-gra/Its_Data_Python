#Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, 
# riempire questa lista con tre oggetti diversi.
#Scrivere, poi, un programma che utilizzi un match statement 
# per classificare gli oggetti presenti nella lista:

oggetti=[]

for x in range(3):
 oggetti.append(input("inserire oggetti: "))

match oggetti:
 case oggetti if oggetti==["penna", "matita", "quaderno"]:
  print("Materiale scolastico")
 case oggetti if oggetti==["pane", "latte", "uova"]:
  print( "Prodotti alimentari") 
 case oggetti if oggetti==["sedia", "tavolo", "armadio"]:
  print( "Mobili")
 case oggetti if oggetti 