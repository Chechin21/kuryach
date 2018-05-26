a = str(input())
j=0
first = -1
end=0

for i in a:
    j+=1
    if i == "@" and first == -1:
        first = j
    if i == "@":
        end = j-1
b = a[first:end]
print(a[:first]+ b[::-1] + a[end:])