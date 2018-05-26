n = int(input())
m = [["" for x in range(2)] for y in range(n-1)]
for i in range(n-1):
    a = input().split(" ")
    m[i][0] = a[0]
    m[i][1] = a[1]
first=[]
level = [["" for x in range(n)] for y in range(n-1)]
level[0][0] = "X"
for j in range(1,n-1):
    for i in m:
        if i[1] in level[j-1]:
            level[j].append(i[0])
for i in m:
    first.append(i[0])
first.append("X")
first.sort()
for i in first:
    num = 0
    for j in level:
        if i in j:
            print(i + " " + str(num))
        num +=1