#Quando usare le regEx + lamda 


import re 

word:list[str]=["abc123","456","hello","98acd"]

only_digits=list(filter(lambda x: re.fullmatch(r"\d+",x),word))

print(only_digits)


##############

#regEx + lambda 

text:str="Price:100 dollars ,Tax: 20 dollars"

new_text=re.sub(r"\d+",lambda m:str(int(m.group())*2),text)

print(new_text)