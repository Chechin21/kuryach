
class Dots:
    def __init__(self,a,b):
        self.a = float(a)
        self.b = float(b)
        self.len = b - a

    def __getitem__(self, item):
        if type(item) is int:

            return(self.a + i + (self.len/ float((item - 1))) for i in range(0,item))
        elif type(item) is slice:
            if not item.step:
                if item.start >= 0:
                    return list(self.a + i for i in range(0, int(self.b) * abs(item.start) +1, int(self.b / float((item.stop - 1)))))[abs(item.start)]
                else:
                    return -list(self.a + i for i in range(0, int(self.b) * abs(item.start) +1, int(self.b / float((item.stop - 1)))))[abs(item.start)]
            elif not item.stop and not item.start:
                return (self.a + i for i in range(0, int(self.b) + 1, int(self.b / float((item.step - 1)))))

            elif not item.stop:
                return (self.a + i for i in
                        list(y for y in range(0, int(self.b) + 1, int(self.b / float((item.step - 1)))))[
                        item.start:])

            elif  not item.start:
                return (self.a + i for i in
                        list(y for y in range(0, int(self.b)*item.stop + 1, int(self.b / float((item.step - 1)))))[
                        :item.stop])

            else:
                if item.start >= 0 and item.stop >= 0:
                    return (self.a + i for i in list(y for y in range(0,int(self.b)*item.stop+1, int(self.b / float((item.step - 1)))))[item.start:item.stop])
                else:
                    return (self.a + i for i in list(y for y in range(- (int(self.b / float((item.step - 1)))) * abs(item.start), 0 , int(self.b / float((item.step - 1))))) + list(y for y in range(0, int(self.b)*item.stop + 1, int(self.b / float((item.step - 1)))))[:item.stop])


a = Dots(-1,1)
print(*a[7])
#print(a[0:7])print(a[2:7])
#print(a[4:7])
#print(a[7:7])
#print(a[-7:7])
#print(*a[1:3:7])
#print(*a[:3:7])
#print(*a[2::7])
#print(*a[::7])
#print(*a[-2:8:7])