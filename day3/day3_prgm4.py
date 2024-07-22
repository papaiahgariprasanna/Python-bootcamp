class Student:
    branch='cse'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {Student.branch} {self.address} {self.email}'
        print()
s1=Student('sana',245,'hyd','sana@gmail.com')
s2=Student('jai',55,'nzb','jai@gmail.com')
print(s1)
print(s2)