import math
class Triangle:
    #x,y,z = 0,0,0
    def __init__(self,x,y,z):

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __len__(self):
        if self.x > self.y + self.z or self.y > self.x + self.z or self.z > self.x + self.y or self.x <= 0 or self.y <= 0 or self.z <= 0:
            return 0
        else:
            return 3
    def __abs__(self):
        if self.x > self.y+self.z or self.y > self.x+self.z or self.z > self.x+self.y or self.x<=0 or self.y<=0 or self.z<=0:
            return 0
        else:
            p = (self.x+self.y+self.z) / 2
            return float(math.sqrt(p*(p-self.x)*(p-self.y)*(p-self.z)))
    def __str__(self):
        if not self.x:
            return 0
        else:
            return "{}:{}:{}".format(self.x,self.y,self.z)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z or self.x == other.y and self.y == other.z and self.z == other.x or self.x == other.z and self.y == other.y and self.z == other.y or self.x == other.x and self.y == other.z and self.z == other.y or self.x == other.z and self.y == other.y and self.z == other.x or self.x == other.y and self.y == other.x and self.z == other.z:
            return True
        else:
            return False
    def __ge__(self, other):

        return abs(self) >= abs(other)

    def __lt__(self, other):
        return abs(self)< abs(other)



#Tri = Triangle(3,4,5), Triangle(5,4,3), Triangle(7,1,1), Triangle(5,5,5), Triangle(7,4,4)#
#for a,b in zip(Tri[:-1],Tri[1:]):
#a = Triangle(3,4,5)
#b = Triangle(5,4,3)
    #print(a if a else b)
   # print("{}={:.2f} {}={:.2f}".format(a,abs(a), b, abs(b)))
  ##  print(a == b)
   # print(a >= b)
   # print(a < b)
#Tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Triangle(7, 4, 4)
#for a, b in zip(Tri[:-1], Tri[1:]):
#    print(a if a else b)
#    print("{}={:.2f} {}={:.2f}".format(a, abs(a), b, abs(b)))
#    print(a == b)
#    print(a >= b)
#    print(a < b)


