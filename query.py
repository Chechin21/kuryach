a = input().split(" ")
n = int(a[0])
m = int(a[1])
result = [0]*n
matrix = [[0 for x in range(n)] for y in range(m)]
for i in range(m):
    a = input().split(" ")
    for j in range(n):
        matrix[i][j] = int(a[j])
for k in range(n):# если умеет только одну задачу, то пусть делает ее
    num=0
    for i in matrix:
       num = i.count(1)
       if num == 1:
           result[i.index(1)]=1
       num += 1

    num = 0
    for i in result:# освобождаем остальных от этой задачи
        if i == 1:
            for i in matrix:
                i[num] = 0
        num += 1

notzerocolumn = [0]*n
notzeroraws = [0]*m
globnum = 0
for i in matrix:
    num = 0
    for j in i:
        if j == 1:
            notzerocolumn[num] = 1
            notzeroraws[globnum] = 1
        num += 1
    globnum += 1
print(result.count(1) + min(notzerocolumn.count(1),notzeroraws.count(1)))
