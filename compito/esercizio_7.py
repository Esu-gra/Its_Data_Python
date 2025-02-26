a=[12,23,4,5,8]
b=[1,5,6,7,9]
c=[]
for i in range(len(a)) :
     c.append(a[i]+b[len(b)-i-1])
print(c)