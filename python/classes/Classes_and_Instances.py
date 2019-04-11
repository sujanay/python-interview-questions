# Python OOP

class Employee:
    pay_raise = 1.04
    num_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + '@company.com'
        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.pay_raise)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.pay_raise = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Sujan','Tamang', 5000)
emp2 = Employee('Jiya', 'Tamang', 6000)

import datetime
my_date = datetime.date(2019, 4, 12)

print(Employee.is_workday(my_date))