

class Student:
    
    def __init__(self, name, id, dept): #works like a constructor
        self.name=name
        self.id=id
        self.dept=dept

if __name__=='__main__':
    st=Student('John', 234, 'CSE')
    
    print(st.name)
    print(st.dept)
    print(st.id)
