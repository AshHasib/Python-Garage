

class Shape:
    def __init__(self,  l,  b, h) :
        self.length=l
        self.bredth=b
        self.height=h
    def getArea(self):
        return self.length*self.bredth
        
    def getVolume(self):
        return self.length*self.bredth*self.height
    
s1=Shape(2, 3, 4)
print(s1.getArea())
print(s1.getVolume())
