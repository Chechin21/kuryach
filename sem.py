class Desc:
    var = 0
    who = 0
    def __set__(self,obj,val):
        #if self.var == 0:
        self.var = 1
        self.who = obj.name
        #else:
        ##    print('het')
#            return self.who

    def __get__(self,obj,cls):
        if self.var == 0:
            self.var = 1
            self.who = obj.name
            #print('het')
            return None
        else:
            #print('het')
            return '<{}>'.format(self.who)

    def __delete__(self, instance):
        if instance.name == self.who:
            self.var = 0
            self.who = 0
        else:
            pass
class Sem:
    lock = Desc()

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

#    def lock(self):
#        if self.fld == 0:
#           self.fld = 1
#            return
#        else:
#            return self.fld

'''
a, b = Sem("A"), Sem("B")
print("Locked:",a.lock) # A взводит опущенный семафор
print("Locked:",a.lock) # Семафор взведён A
print("Locked:",b.lock) # Семафор взведён A
del(b.lock)             # B пытается сбросить семафор
print("Locked:",b.lock) # Семафор взведён A
print("Locked:",a.lock) # Семафор взведён A
del(a.lock)             # А сбрасывает семафор
print("Locked:",b.lock) # B взводит опущенный семафор
print("Locked:",a.lock) # Семафор взведён B
'''