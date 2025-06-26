
# mcd con il metodo di Euclide 

# def mcd(x:int,y:int)->int:
#     while y!=0:
#         x,y=y,x%y    
#     return x





def mcd(x: int, y: int) -> int:
    divisori_x = {i for i in range(1, x+1) if x % i == 0}
    divisori_y = {i for i in range(1, y+1) if y % i == 0}
    comuni = divisori_x & divisori_y
    return max(comuni) if comuni else 1
   


print(mcd(60,40))


        
            


    
    