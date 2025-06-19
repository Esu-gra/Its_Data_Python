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

         self.den=5
    
    def get_numeratore(self):
        return self.num
    def get_denominatore(self):
        return self.den
    
    
    
    def value(self):
        return round(self.num/self.den) 
        
    def __str__(self):
        return    f"{self.num}/{self.den}"
    


f1 = Frazione(10, 4)
print(f1)             
print(f1.value())     

f2 = Frazione("a", 0)
print(f2)            
print(f2.value()) 
