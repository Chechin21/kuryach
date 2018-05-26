
a = [ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]

#print(list(zip(*a)))

for i in range(3):
  a = list(zip(*reversed(a)))

for i in a:
  print(i)

#for i in a:
#  a[i] = list((*reversed(i))

#print(list(zip(*a)))