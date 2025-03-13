a=int(input("inserire il primo numero: "))
b=int(input("inserire il secondo numero: "))
sum=0
i=a


if a<b:
      if a>0 and b>0:
         if a%1==0 and b%1==0:
            sum=0
            i=a
            while i>b:
                i=i+1
                sum=sum+i
            print(sum)
              

         elif b<a:
            print("a e b devono essere interi")
      elif a <0 and b <0:
         print("a e b devono essere positivi")
elif a%1!=0 and b%1!=0:
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