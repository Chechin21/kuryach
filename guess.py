class A:
    def __init__(self,a):
        self.val = a
    def __add__(self,other):
        if isinstance(self,C):
            return B(self.val + other.val)
        else:
            return A(self.val + other.val)
    def __radd__(self,other):
        if isinstance(self,C):
            return B(self.val + other.val)
        else:
            return A(self.val + other.val)
    def __str__(self):
        return '/{}/'.format(self.val)

class B:
    def __init__(self,a):
        self.val = a
    def __str__(self):
        return '|{}|'.format(self.val)
    def __rmul__(self, other):
        if isinstance(other,A):
            return B(other.val * self.val)
        else:
            return B(other.val * self.val)

    def __mul__(self, other):
        if isinstance(other, A):
            return B(other.val * self.val)
        else:
            return B(other.val * self.val)
    #def __mul__(self, other):
    #    return B(other.var * self.val)

class C(B,A):
    def __init__(self,a):
        self.val = a

'''
a, b, c, d = A(2), B(3), C(4), C("Op")
print(a,b,c, a+b+c, a*b*c, a*b*d)
print(*(o+p for o in (a,b,c) for p in (a,b,c) if not o==b==p))

#print(b+c)
#print(c+a)
#print(c+b)
#print(c+c)

print(*(o*p for o in (a,b,c,d) for p in (a,b,c,d) if not o==a==p and not o==d==p))
print(*(isinstance(e,T) for e in (a,b,c) for T in (A,B,C)))
print(*(a in T.__dict__.keys() for a in ('__add__','__mul__','__str__') for T in (A,B,C)))
'''