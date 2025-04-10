#Lambda : piccola funznione che implementa una piccola logica 

#syntax 

#lambda arguments:expression

r= lambda a,b:a+b

#puo avere diversi argomenti ma  una sola operazione 


#general form 

from typing import Callable


multiply=[12,34]
multiply:Callable[[int,int],int]=lambda a,b:a*b
print(multiply(12,3))


# 1 example 

square: Callable[[int,int],int]=lambda x: x**2

print(square(2))

#2 example 

mult:Callable[[float,float],float]=lambda a,b:a*b

print(mult(1.3,4.5))

#3 example 

positive_negative:Callable[[int,int],int]=lambda x: "Positivo" if x>0 else  "Zero o negativo"
print(positive_negative(12))



#example 4

#filter()
nums:list[int]=[1,2,3,4,5]
evans:list[int]=list(filter(lambda x: x%2==0,nums))

print(evans)



#sorted()
names:list[str]=["Alice","Pola","Nonna"]
sorted_by_lenght=sorted(names,key=lambda name: len(name))
print(sorted_by_lenght)


#Quando usare lambda : 
# -quando non vuoi definire una funzione
#-


