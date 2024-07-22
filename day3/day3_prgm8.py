class Employee:
    def _init_(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary      #private data

    def get_salary(self):
       return self.__salary


    def Empdisplay(self):
       print(self.name,self.role)
class Company(Employee):
    def _init_(self,cname,loc):
       self.cname=cname
       self.loc=loc 

    def Comdisplay(self):
       print(self.cname,self.loc) 

    def _hiring(self):
       print('hiring for the manager role')     

cobj=Company('wipro','gachibowli')
eobj=Employee('srivani','mitty',100000)
eobj.Empdisplay()
print(cobj._hiring())
