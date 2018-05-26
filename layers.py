num = int(input())
a = input().split(" ")
a.sort(key=lambda x:int(x))
max = int(a[1])-int(a[0])
i = 2
while i < num:
    if num-1 != i:
        if int(a[i]) - int(a[i-1]) < int(a[i+1]) - int(a[i]):
            max += int(a[i]) - int(a[i-1])
            i+=1
        else:
            max += int(a[i+1]) - int(a[i])
            i += 2
    else:
        max += int(a[i]) - int(a[num-2])
        i+=1

print(max)
