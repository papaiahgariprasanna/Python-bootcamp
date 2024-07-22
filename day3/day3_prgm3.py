class Student:
    branch='cse'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def display(self):
        print('name is:',self.name)
        print('roll is:',self.roll)
        print('branch is:',Student.branch)
        print('address is:',self.address)
        print('email is:',self.email)
s1=Student('sana',245,'hyd','sana@gmail.com')
s2=Student('jai',55,'nzb','jai@gmail.com')
s1.display()
s2.display()