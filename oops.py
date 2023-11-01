class employee:
    FirstName:str="sai"
    LastName:str="bhavani"
    def FullName(self):
        return self.FirstName+" "+self.LastName
emp=employee()
print(emp.FullName())


#access modifier
#global scope
class employee:
    firstName ="sai"
    lastName ="bhavani"
emp=employee()
print(emp.firstName)

#partially private scope
class employee:
    _firstName ="sai"
    _lastName ="bhavani"
emp=employee()
print(emp._firstName)

#strictly private scope
class employee:
    __firstName ="sai"
    __lastName ="bhavani"
emp=employee()
print(emp.__firstName)



