a = [['.','.','.','y','y','y','.','.','.','.','.','.'],
     ['.','.','.','y','U','y','.','.','.','.','.','.'],
     ['.','.','.','y','y','y','.','.','.','.','.','.'],
     ['b','b','b','r','r','r','g','g','g','o','o','o'],
     ['b','L','b','r','F','r','g','R','g','o','B','o'],
     ['b','b','b','r','r','r','g','g','g','o','o','o'],
     ['.','.','.','w','w','w','.','.','.','.','.','.'],
     ['.','.','.','w','D','w','.','.','.','.','.','.'],
     ['.','.','.','w','w','w','.','.','.','.','.','.']]



#print(a[3:6][2][2])

def Lrev(bool) :
    b = [a[0][3], a[1][3], a[2][3]]
    r = [a[3][0:3],a[4][0:3],a[5][0:3]]
    for i in range(0,3):
        r = list(zip(*reversed(r)))

    for i in range(0,3):
        a[i+3][0:3] = r[i]

        a[i][3] = a[i+3][3]
        a[i+3][3] = a[i+6][3]
        a[i+6][3] = a[5-i][11]
        a[5-i][11] = b[i]
    if bool == True:
        for y in a:

            print(''.join(str(i) for i in y))
        print()

def R(bool) :
    b = [a[0][5], a[1][5], a[2][5]]
    r = [a[3][6:9], a[4][6:9], a[5][6:9]]
    r = list(zip(*reversed(r)))

    for i in range(0, 3):
        a[i+3][6:9] = r[i]

        a[i][5] = a[i + 3][5]
        a[i + 3][5] = a[i + 6][5]
        a[i + 6][5] = a[5 - i][9]
        a[5-i][9] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def Rrev(bool) :
    b = [a[0][5], a[1][5], a[2][5]]
    r = [a[3][6:9], a[4][6:9], a[5][6:9]]
    for i in range(0,3):
        r = list(zip(*reversed(r)))
    for i in range(0, 3):
        a[i + 3][6:9] = r[i]

        a[i][5] = a[5 - i][9]
        a[5 - i][9] = a[i + 6][5]
        a[i + 6][5] = a[i + 3][5]
        a[i + 3][5] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def L(bool) :
    b = [a[0][3], a[1][3], a[2][3]]
    r = [a[3][0:3], a[4][0:3], a[5][0:3]]
    r = list(zip(*reversed(r)))

    for i in range(0,3):

        a[i + 3][0:3] = r[i]

        a[i][3] = a[5-i][11]
        a[5-i][11] = a[i+6][3]
        a[i+6][3] = a[i+3][3]
        a[i+3][3] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def UPrev(bool) :
    b = [a[3][0],a[3][1],a[3][2]]
    r = [a[0][3:6], a[1][3:6], a[2][3:6]]
    for i in range(0,3):
        r = list(zip(*reversed(r)))
    for i in range(0,3):
        a[i][3:6] = r[i]


        a[3][i] = a[3][9+i]
        a[3][9+i] = a[3][6+i]
        a[3][6+i] = a[3][3+i]
        a[3][3+i] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def UP(bool) :
    b = [a[3][0],a[3][1],a[3][2]]
    r = [a[0][3:6],a[1][3:6],a[2][3:6]]
    r = list(zip(*reversed(r)))

    for i in range(0,3):
        a[i][3:6] = r[i]

        a[3][i] = a[3][3+i]
        a[3][3+i] = a[3][6+i]
        a[3][6+i] = a[3][9+i]
        a[3][9+i] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def Down(bool) :
    b = [a[5][0],a[5][1],a[5][2]]
    r = [a[6][3:6], a[7][3:6], a[8][3:6]]
    r = list(zip(*reversed(r)))
    for i in range(0,3):
        a[i+6][3:6] = r[i]

        a[5][i] = a[5][9+i]
        a[5][9+i] = a[5][6+i]
        a[5][6+i] = a[5][3+i]
        a[5][3+i] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()


def Downrev(bool) :
    b = [a[5][0],a[5][1],a[5][2]]
    r = [a[6][3:6], a[7][3:6], a[8][3:6]]
    for i in range(0,3):
        r = list(zip(*reversed(r)))
    for i in range(0,3):
        a[i+6][3:6] = r[i]


        a[5][i] = a[5][3+i]
        a[5][3+i] = a[5][6+i]
        a[5][6+i] = a[5][9+i]
        a[5][9+i] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def Front(bool):
    b = [a[2][3],a[2][4],a[2][5]]
    r = [a[3][3:6], a[4][3:6], a[5][3:6]]
    r = list(zip(*reversed(r)))
    for i in range(0,3):
        a[i+3][3:6] = r[i]


        a[2][i+3] = a[5-i][2]
        a[5-i][2] = a[6][5-i]
        a[6][5-i] = a[i+3][6]
        a[i + 3][6] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def Frontrev(bool):
    b = [a[3][2],a[4][2],a[5][2]]
    r = [a[3][3:6], a[4][3:6], a[5][3:6]]
    for i in range(0,3):
        r = list(zip(*reversed(r)))
    for i in range(0,3):
        a[i+3][3:6] = r[i]

        a[i+3][2] = a[2][5-i]
        a[2][5-i] = a[5-i][6]
        a[5-i][6] = a[6][i+3]
        a[6][i + 3] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def Back(bool):
    b = [a[3][0],a[4][0],a[5][0]]
    r = [a[3][9:12], a[4][9:12], a[5][9:12]]
    r = list(zip(*reversed(r)))

    for i in range(0,3):
        a[i+3][9:12] = r[i]


        a[i+3][0] = a[0][5-i]
        a[0][5-i] = a[5-i][8]
        a[5-i][8] = a[8][i+3]
        a[8][i + 3] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def Backrev(bool):
    b = [a[0][3],a[0][4],a[0][5]]
    r = [a[3][9:12], a[4][9:12], a[5][9:12]]
    for i in range(0, 3):
        r = list(zip(*reversed(r)))
    for i in range(0,3):
        a[i+3][9:12] = r[i]

        a[0][i+3] = a[5-i][0]
        a[5-i][0] = a[8][5-i]
        a[8][5-i] = a[i+3][8]
        a[i + 3][8] = b[i]
    if bool == True:
        for y in a:
            print(''.join(str(i) for i in y))
        print()

def L2():
    L(0)
    L(1)

def R2():
    R(0)
    R(1)

def UP2():
    UP(0)
    UP(1)

def Down2():
    Down(0)
    Down(1)

def Back2():
    Back(0)
    Back(1)

def Front2():
    Front(0)
    Front(1)




command = input().split(' ')

for y in a:
    print(''.join(str(i) for i in y))
print()

for i in command:
    if i == 'R':
        R(1)
    if i == 'R\'':
        Rrev(1)
    if i == 'L':
        L(1)
    if i == 'L\'':
        Lrev(1)
    if i == 'R2':
        R2()
    if i == 'L2':
        L2()
    if i == 'U':
        UP(1)
    if i == 'U\'':
        UPrev(1)
    if i == 'U2':
        UP2()
    if i == 'D':
        Down(1)
    if i == 'D\'':
        Downrev(1)
    if i == 'D2':
        Down2()
    if i == 'B':
        Back(1)
    if i == 'B\'':
        Backrev(1)
    if i == 'B2':
        Back2()
    if i == 'F':
        Front(1)
    if i == 'F\'':
        Frontrev(1)
    if i == 'F2':
        Front2()


