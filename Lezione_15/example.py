# file=open("Lezione_15/example.txt") #"r" -> scrittura ,"w"->leggere,"a"->append 

# print(file)     -------> modo di leggere e chiudere i file non conveniente 
              
# file.close()



with open("Lezione_15/example.txt","w") as file:
    stringa:str="bella"
    file.write(stringa)
    pass # -----> la maggior parte delle volte si usa questo metodo 