

def mcd(x,y)->int:
    max_int=1
    end=0
    if x>y:
        end=x
    else:
        end=y
    div=[]

    for i in range(1,end +1):
        if x%i==0 and y%i==0:
            div.append(i)
            return max(div)
        
            


    
    