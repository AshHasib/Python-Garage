

class Employee:
    
    def __init__(self, fname,  lname, sal):
        self.fname=fname
        self.lname=lname
        self.sal=sal
    

rahim= Employee('rahim', 'uddin', 300)
print(rahim.__dict__) #printing the namespace of the instance
        
