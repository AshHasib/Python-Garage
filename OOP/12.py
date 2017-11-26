class Student:
    inc=100
    def __init__(self,name, id, fee, ):
        
        self.name=name
        self.id=id
        self.fee=fee
        
    def feeRaise(self):
        return self.fee+self.inc
    

if __name__=='__main__' :
    st1=Student('John', 1,  500)
    print(st1.feeRaise())
    
    print(Student.inc)
    print(Student.feeRaise(st1))
