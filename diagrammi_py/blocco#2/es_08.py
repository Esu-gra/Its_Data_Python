a=int(input("inserire il primo numero: "))
b=int(input("inserire il secondo numero: "))
sum=0
i=a

while True:
   if a<b:
      if a>0 and b>0:
         if a%1==0 and b%1==0:
            sum=0
            i=a
            if i>b:
               print(sum)
            else:
               sum=sum+i
               i=i+1

         else:
            print("a e b devono essere interi")
      else:
         print("a e b devono essere positivi")
   else:
      print("a deve essere minore di b")

       


      
   

'''
a = int(input("Inserire il primo numero: "))
b = int(input("Inserire il secondo numero: "))

if a >= b:
    print("a deve essere minore di b")
    exit()

if a <= 0 or b <= 0:
    print("a e b devono essere positivi")
    exit()
    
if not (isinstance(a, int) and isinstance(b, int)):
    print("a e b devono essere interi")
    exit()

# Calcolo della somma dei numeri da a a b
sum = 0
for i in range(a, b + 1):
    sum += i

print("La somma dei numeri da", a, "a", b, "è:", sum)
'''