class Vector:
    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __add__(self,A):
        return Vector(self.x + A.x  ,self.y + A.y , self.z + A.z )
    #def __add__(self,A):
    #    return self.x + A.x  ,self.y + A.y , self.z + A.z
    def __sub__(self,A):
        return  Vector(self.x - A.x , self.y - A.y , self.z - A.z )
    def __mul__(self,A):
        return  Vector(self.x * A , self.y * A , self.z * A )
    def __rmul__(self,A):
        return  Vector(self.x * A , self.y * A , self.z * A )
    def __truediv__(self,A):
        return  Vector(self.x / float(A) , self.y / float(A) , self.z / float(A) )
    def __matmul__(self,A):
        return self.x * A.x + self.y * A.y + self.z * A.z
    def __str__(self):
        return  "{:.2f}:{:.2f}:{:.2f}".format(self.x,self.y ,self.z )

A = Vector(1,2,3)
B = Vector(-1,3,-2)
C = Vector(7,3,5)
#print("A, B, C:", A, B, C)
#print(A, "+", B, "=", A+B)

#print(A, "-", C, "=", A-C)
#print(A, "*", 2, "=", A*2)
#print(2, "*", B, "=", 2*B)
#print(C, "/", 3, "=", C/3)
#print(B, "@", C, "=", "{:.2f}".format(B@C))
#print(Vector(2,4,10)/2@(Vector(2,2,2)-Vector(3,4,1)))
#print(type( Vector(2,3,4)))