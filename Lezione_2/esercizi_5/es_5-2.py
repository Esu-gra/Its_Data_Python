
#esercizio 5-2

# test for equality and inequality whit strings

w="Paolo"
e="paolo"

# print(w==e)

# test using the lower metod 
print(w.lower())

#numerical test  involving  equality and inequality , greater than and less
#greater than or equal to , and less thean  or equal to

#uguaglianza 

for i in range(23):
    if  i%2==0:
        print(i)
        



#disuguaglianza
'''
for y in range(8):
    if y!=2:
       print("Null")
    else:
        print(y)

        '''

#maggiore e minore
'''
n=int(input("inserire età per partecipare al party: "))

if n > 23:
    print("Puoi entrare al party")
elif n < 23:
    print("Troppo piccolo per il party")
elif n>=23:
    print("Puoi entrare al party")
    '''



l=["pane","formaggio",34,23]

if "acqua" in l:
    print(True)
else:
    print(False)