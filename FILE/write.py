

fpt=open('Sample.txt', 'w')

class Student:
    def __init__(self, name, id):
        self.name=name
        self.id=id
        
    def Display(self):
        print(self.name, end='\t')
        print(self.id)


if __name__=='__main__' :
    St1=Student('Hasib', 54)
    St2=Student('Sabbir', 55)
    
    
    fpt.write(str(St1.Display()))
    fpt.write(str(St2.Display()))
    fpt.write('asdhaosdjasa')
    
    fpt.close()
    
