# Class variables can be accessed by instances of a class
#if the value is changed by the class, it works for all instances
#if the value is changed by an instance, it works for that instance only
class Employee:
    rise=100
    numOfEm=0
    def __init__(self, name, money):
        
        self.name=name
        self.money=money
        Employee.numOfEm+=1
        
    def raiseAmount(self):
        return (self.money+self.rise)
    
rahim=Employee('Rahim Uddin', 500)
karim=Employee('Karim Reza', 600)
'''
print(rahim.name)
print(rahim.money)
print(rahim.raiseAmount())
print(rahim.rise)
print(Employee.rise)
print(Employee.raiseAmount(rahim))


print(rahim.__dict__)
print(Employee.__dict__)
'''
print(rahim.rise)
print(rahim.__dict__)
print(Employee.rise)
rahim.rise=200
print(rahim.__dict__)
print(Employee.rise)
print(rahim.rise)
print(Employee.numOfEm)
