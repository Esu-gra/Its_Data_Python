#exemple

#list comprehension 

#syntax : [expression for item in iterable if condition]

squres=[]

for x in range(10):
    if x%2==0:
        squres.append(x**2)

#comprehension  
squres=[x**2 for x in range(10) if x%2==0]


##################################################

names:list[str]=["lollo","pola","pippo"]

uppercase_name:list[str]=[name.upper() for name in names]

print(uppercase_name)

#####################################################

#set

word = ["hi","jbcjk","hi","buu"]

unique_lengths={len(words) for words in word}
print(unique_lengths)

# dictionary 

squares_dict={x:x**2 for x in range(5)}
print(squares_dict)

