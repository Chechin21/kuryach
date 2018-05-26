class Normal:
    def __init__(self,start):
        self.start = start
    def what(self):
        return self.start
    def swap(self,other):
        a = other.start
        other.start = self.start
        self.start = a

class Double:
    def __init__(self,start):
        self.start = start * 2
    def what(self):
        return self.start * 2
    def swap(self,other):
        a = other.start * 2
        other.start = self.start * 2
        self.start = a

