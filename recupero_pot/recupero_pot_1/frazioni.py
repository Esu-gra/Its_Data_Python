from mcd import mcd

class Frazione:
    def __init__(self,num:int,den:int):
        self.set_numeratore(num)
        self.set_denominatore(den)        

    def set_numeratore(self,x:int):
       if isinstance(x,int):
           
           self.num=x
       else:
           self.num=13

       
    
    def set_denominatore(self,y:int):
         if  isinstance(y,int) and y!=0:
           
            self.den=y

         else:
             self.den=5
    
    def get_numeratore(self):
        return self.num
    def get_denominatore(self):
        return self.den
    
    
    
    def value(self):
        return round(self.num/self.den,2) 
        
    def __str__(self):
        return    f"{self.num}/{self.den}"
    






def semplificata(list_fraz:list[Frazione])->list[Frazione]:
    irriducibili:list[Frazione]=[]
    for i in list_fraz:
        if   isinstance(i,Frazione):
            n=i.get_numeratore()
            d=i.get_denominatore()
            divisore=mcd(n,d)
            nuova_frzione=Frazione(n//divisore,d//divisore)
            irriducibili.append(nuova_frzione)
    return irriducibili





# if __name__ == "__main__":
#     f1 = Frazione(8, 4)     
#     f2 = Frazione(3, 7)      
#     f3 = Frazione(6, 9)      
#     f4 = "errore"            

#     lista = [f1, f2, f3, f4]
#     lista_irriducibili = semplificata(lista)
   
  

# for f in lista_irriducibili:
#         print(f)



#Ho dovuto commentare queste righe di codice perche,
#quando quando vado a runnare il codice del file fractionCompare, mi
# da errore