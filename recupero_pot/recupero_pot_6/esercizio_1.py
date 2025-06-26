def  recursivePalindrome(parametro:str)->bool:
    parametro=parametro.replace(" ","")

    if len(parametro)<=1:
        return  True
    
    if parametro[0]!=parametro[-1]:
        return False
    
    return recursivePalindrome(parametro[1:-1])
    

print(recursivePalindrome("casa"))