

def mcd(x,y)->int:
    div_x_y = set()
    for i in range(1,x+1):
        if i%2==0 and x%i==0:
            div_x_y.add(i)
        
    for i in range(1,y+1):
            if i%2==0 and y%i==0:
              div_x_y.add(i)
    return max(div_x_y)
  

   


print(mcd(4,6))



        
            


    
    