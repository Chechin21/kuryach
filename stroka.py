class Stroka(str):
    #def __init__(self,str):
    #    self.var = str
    def __neg__(self):
        return self[::-1]
    def __mul__(self, other):
        if type(other) == int:
            self = str.__mul__(self,other)
            return Stroka(self)
        c = Stroka()
        for i in self:
            for j in other:
                c += '{}{}'.format(i,j)
        return Stroka(c)
    def __pow__(self, power, modulo=None):
        a = self
        for i in range(power-1):
            a *= self
#        print(type(a))
        return a
#print(dir(str))
#a, b, c, d = Stroka("wer"), Stroka("ASDF"), Stroka("12"), Stroka(":,")
#print(a+b)
#print(c*4)
#print(b[2:])
#print(a*b)
#print(c**3)
#print(a*c*d)