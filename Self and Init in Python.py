class Employee:

    noOfLeaves = 8

    def __init__(self,name,salary,role,city):
        self.name = name
        self.salary = salary
        self.role = role
        self.city = city

    def printDetails(self):
        return f'Hii Your salary is {self.salary} and your name is {self.name} and your role is this {self.role}'

# Harry = Employee()
# Harry.name = 'Harry'
# Harry.salary = 12000
# Harry.role = 'instructor'

# Ravi = Employee()
# Ravi.name = 'Ravi'
# Ravi.salary = 12000
# Ravi.role = 'Cordinator'

# print(Harry.printDetails())
# print(Ravi.printDetails())

Harry = Employee('Harry',12000,'Instructor','Mumbai')
Ravi = Employee('Ravi',12000,'Cordinator','Ganganagar')
Rashmi = Employee('Rashmi',14000,'Engineer','Patna')
Nishant = Employee('Nishat',24000,'Developer','Jaipur')
print(Harry.salary)
print(Rashmi.city)
print(Nishant.city)


