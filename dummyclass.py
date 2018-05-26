class Delay:
    def __init__(self,slot):
        self.slot = slot
    def delay(self,new):
        a = self.slot
        self.slot = new
        return a

