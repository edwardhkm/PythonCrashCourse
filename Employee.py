class Employee:
    def __init__(self, first, last, annual_salary):
        self.firstname = first
        self.lastname = last
        self.annual_salary = int(annual_salary)

    def give_raise(self, pay_raise=5000):
        self.annual_salary += pay_raise
        return self.annual_salary


# emp = Employee('ho', 'ed', 100)
# print(emp.give_raise())