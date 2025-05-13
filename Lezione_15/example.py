# file=open("Lezione_15/example.txt") #"r" -> scrittura ,"w"->leggere,"a"->append 

# print(file)     -------> modo di leggere e chiudere i file non conveniente 
              
# file.close()


#lettura di file di testo


# with open("Lezione_15/example.txt","w") as file:
#     stringa:str="bella"
#     file.write(stringa)
#     pass # -----> la maggior parte delle volte si usa questo metodo 






#lettura file json 

import json

# PATH:str="Lezione_15/config.json"
# mode:str="r"  #modalità di lettura 

# with open(PATH,mode=mode) as file:
#     config:dict=json.load(file)

#     print(config)




#creare e leggere un file.json insesistente

# PATH:str = "Lezione_15/config_1.json"
# mode :str="w"

# with open(PATH,mode=mode) as file:
#     comfig_1:dict={"nome":"2048","versione":"1.1.42","os":"Android 16.1.2"}
#     json.dump(comfig_1,file,indent=4)





#1 crea un file json usando i comandi touch , e nano ,leggete i file appena creato e stampate un valore 
#2 crea un file json da python salvando un dizionario a vostra scelta 
#3 crea un file json usando touch e nano  che contiene codici fiscali come chiavi e come vlaori dizionari che contengono nome,cognome ed età della persona (almeno due persone)
   #e poi modificare  aggiungendo una persona 



import json 

#esercizio1

# PATH:str="esempio_1.json"
# mode="r"
# with open(PATH,mode=mode) as file:
#     config:dict=json.load(file)

#     print(config)



#esercizio2
PATH:str="Lezione_15/esercizio/esempio_2.json"
mode="w"

with open(PATH,mode=mode) as file:
    dict_1:dict={"nome":"Esu",
                 "cognome":"Grappa",
                 "età":234}
    json.dump("dict_1",file,indent=4)
    

#esercizio3
