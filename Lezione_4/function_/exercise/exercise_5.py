def add_one(a):
    a=a+1
    return a

print(add_one(34))


#########################


def ad_one_list(*args:int):
    new_list=[]
    for i in args:
      
        new_list.append(  add_one(i))
    return new_list

print(ad_one_list(12,34,56))






