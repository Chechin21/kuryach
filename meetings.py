a = input().split(" ")
n = int(a[0])
m = int(a[1])
result = [n]
matrix = list()
for i in range(m):
    matrix.insert(i, input())
matrix.sort(key = lambda x: x.count("1"))
for i in matrix:
    print(i)
matrix.sort()
print()
for i in matrix:
    print(i)

#for i in range(n):
#    result[i] = 0
#for i in matrix:
#    num = i.count("1")
#    if num == 1:
#        result[i.find("1")] = 1
#    else:
