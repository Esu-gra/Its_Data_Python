#Character class

#[...]  --> match gr[ae]y ---> gray or grey 

#Ranges : 
#[a-z]---> tutti i caratteri minuscoli da a-z

#[0-9] ---> tutti i numeri da 0-9


#Negation

#[^abc] ---> matcha tutti tranne a,b,c


#combineng 






#\d ---> equivale a dire [0-9]
#\d\d ---> --->due cifre da 0 a 9


#\D --> Non digit 



#\w --> Word character 

#\W--->

#\s--->
#\S--->Non-Whitspace character



#Come usare RegEX

import re 

# text:str="My email is esu@gmail.com"
# result:list[str]=re.findall(r'\S+@\S+',text)
# print(result)


#########

text_2=str="Roma Paris"

result_2=re.match(r'[A-Z][a-z]+',text_2)
print(result_2.group()) #output Roma


############


#ricerca numeri 

tex_3=str="I have 23  cats and 3 dog"
nummbers:list[str]=re.findall(r'\d+',tex_3)
print(nummbers)#---> output ['23', '3']


tex_3=str="I have 23  cats and 3 dog"
nummbers:list[str]=re.findall(r'\d',tex_3)
print(nummbers)  #------->output    ['2', '3', '3']



#ricerca 