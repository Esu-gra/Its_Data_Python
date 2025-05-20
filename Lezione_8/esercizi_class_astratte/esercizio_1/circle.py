from shape import Shape
import math

class Circle(Shape):
    
     def __init__(self,r):
           self.r=r
        
     def area(self):
           return f"Area :{math.pi*self.r**2}"
      
     def perimeter(self):
           return f"Perimetro: {2*math.pi * self.r}" 
     



c=Circle(5)
print(c.perimeter())