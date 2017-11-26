

class Employee:
    def __init__(self,  first, last):
        self.first=first
        self.last=last
    
    def fullName(self):
        print(self.first + ' '+ self.last)

emp=Employee('hasib', 'Ashad')
Employee.fullName(emp) # accessing methods through the class itself
        
