class Employee:
    raise_amt = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(">>> ", emp.fullname)

dev1 = Developer('Sujan', 'Tamang', 5000, 'Python')
dev2 = Developer('Jiya', 'Tamang', 6000, 'GO')
mgr1 = Manager('Dummy', 'Tommy', 9000, [dev1])

print(mgr1.email)
print(dev1.email)
print(dev2.email)
print()
print("Developer subclass of Employee? ", issubclass(Developer, Employee))
print("Manager subclass of Employee? ", issubclass(Manager, Employee))
print("Employee subclass of Employee? ", issubclass(Employee, Employee))
print("Employee subclass of Manager? ", issubclass(Employee, Manager))
print()
print("dev1 instance of Developer?", isinstance(dev1, Developer))
print("mgr1 instance of Developer?", isinstance(mgr1, Developer))
print("dev1 instance of Employee?", isinstance(dev1, Employee))
print("mgr1 instance of Employee?", isinstance(mgr1, Employee))
