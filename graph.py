i = input().split(" ")
x = float(i[0])
y = float(i[1])
a = True
if (0.5*x*x + y*y) > 1:
    a = False

if ((x-0.5)*(x-0.5) + y*y) < 0.3:

    a = False
if ((x+0.5)*(x-0.5) + y*y) < 0.3:
    a = False

if (y > (0.5*abs(x) + 0.5)):
    a = False

if a:
    print("YES")
else:
    print("NO")