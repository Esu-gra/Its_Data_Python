class Alieno:

   def __init__(self,galaxy:str):
      self.setGalaxy(galaxy)
    
   def setGalaxy(self,galaxy:str)->None:
      if galaxy:
         self.galaxy=galaxy
      else:
         return print("erorre")
      
   def getGalaxy(self)->str:
       return self.galaxy

   def speak(self)->None:
      print("bedwehdoa")      
    
   def __str__(self)->str:
       return f"\nalieno proveniente dalla galassia {self.getGalaxy()}"