from shape import Shape


class Rectangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    
    def area(self):
        return f"Area rettangolo: {self.b * self.h}"
    def perimeter(self):
        return f"Perimetro rettangolo: {(self.b*self.h)*2}"
    



r=Rectangle(4,6)

print(r.area())
print(r.perimeter())