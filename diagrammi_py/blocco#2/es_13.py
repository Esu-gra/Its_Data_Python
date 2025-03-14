x=int(input("inserire numero x: "))
y=int(input("inserire numero y: "))
z=int(input("inserire numero z: "))
while True:
 if x%1==0 and x>0:
    if y%1==0 and y>0:
        if z%1==0 and z>0:
            if (x+y+z)%2==0 and x%3==0 and y%5==0 and z%7==0:
                print("Regole rispettate")
            else:
                print("Regole non risspettate")
        else:
            print("z deve essere intero e positivo")
    else:
        print("y deve essere intero e positivo")
 else:
    print("x deve essere intero e positivo")