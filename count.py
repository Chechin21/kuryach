a = eval(input())
dict = dir(a)
count = 0
#print(type(a))
if isinstance(a,type):
    for i in range(len(dict)):
        if isinstance(a.__class__.__getattribute__(a,dict[i]),int):
        #if type(a.__getattribute__(dict[i])) == int:
            count+=1

else:
    for i in range(len(dict)):
        #if isinstance(a.__getattribute__( dict[i]), int):
        if type(a.__getattribute__(dict[i])) == int:
            count += 1
print(count)
