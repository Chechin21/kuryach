class Unary:
        def __init__(self,a):
            self.a= a
        def __str__(self):
            return self.a
        def __len__(self):
            return len(self.a)
        def __iter__(self):
            #self.a = Unary(self.a)
            #x = len(self.a)
            return (Unary(y) for y in self.a)
        def __ior__(self, other):
            #print(self.a)
            #print(other.a)
            self.a += other.a
            return self
        def __pos__(self):
            self.a += '|'
            return self
        def __invert__(self):
            self.a = self.a[:int(len(self)/2)]
            return self




#a = Unary("||")
#b = Unary("||||")
#print(a, b)
#a |= b
#print(a)
#print(~a)
#for c in a:
#    print("  ",c)
#    print(". ",+c)
#    print("..",+c)
#~a
#~a
#print("Error" if a else a is a)
