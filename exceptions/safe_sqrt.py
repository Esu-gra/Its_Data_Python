import math
def safe_sqrt(n:int):
    try:
        math.sqrt(n)
    
    except ValueError as error:
        print(error)



safe_sqrt(-2)