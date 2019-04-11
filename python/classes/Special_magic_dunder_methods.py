class Employee:
    raise_amt = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'
        Employee.num_of_employees += 1

    def __gt__(self, other):
        if self.pay > other.pay:
            return True
        return False

    def __repr__(self):
        return "Employee ({} - {} {})".format(self.first, self.last, self.email)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp1 = Employee('Sujan', 'Tamang', 3450)
print(emp1.__repr__())