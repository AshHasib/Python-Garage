class Employee:
        def __init__(self, fName='janina', lName='janina', salary=0):
            self.fName=fName
            self.lName=lName
            self.salary=salary
        
        def fullName(self):
            print(self.fName + " " +self.lName)
            
if __name__ == '__main__' :
    em1=Employee('Hasib', 'Ashad', '60000')
    
    em1.fullName()
