class Student :
    
    def __init__(self, name, id):
        
        self.name=name
        self.id=id
        
    def Display(self):
        print(self.name), 
        print(self.id)
        

st1=Student('Hasib', 54)
st2=Student('Ashad', 54)

st1.Display()
st2.Display()
