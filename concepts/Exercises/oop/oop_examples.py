import datetime
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first.lower() +'.'+self.last.lower()+'@company.com'
        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # you can use Employee.raise_amount if amount will never be changed for specific instances

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alternative Constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()  == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay, prog_lang)
        self.prog_lang = prog_lang


print("Number of Employees:", Employee.num_of_emps)

print("\n***************************************************\n\nInstance Variables and methods\n")
emp_1= Employee('Arka', 'Roy', 50000)
emp_2= Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name())
print(emp_2.full_name())
print(Employee.full_name(emp_1))


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print("\n***************************************************\n\nClass Variables\n")
print("Before")
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06
print("After")
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
del emp_1.raise_amount
# print(emp_1.__dict__)
# print(Employee.__dict__)
print("Number of Employees:", Employee.num_of_emps)

print("\n***************************************************\n\nClass Methods\n")
Employee.set_raise_amt(1.1)
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
emp_1.set_raise_amt(1.2)
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


print("\n***************************************************\n\nStatic Methods\n")

my_date  = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))


print("\n***************************************************\n\nInheritence\n")
dev_1= Employee('Trina', 'Roy', 50000)
dev_2= Developer('Test', 'Employee', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(dev_1.raise_amount)
print(dev_2.raise_amount)
