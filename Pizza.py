from abc import ABC, abstractmethod
import Surprisable
from Rankable import Rankable


class Pizza(Rankable, ABC):
    @abstractmethod
    def __init__(self, pizza_id, name, address, employees, phoneNumber):
        self.pizza_id = pizza_id
        self.name = name
        self.address = address
        self.employees = employees
        self.phone_number = phoneNumber
        self.store_rank = None

    def get_number_of_employees(self):
        return len(self.employees)

    def calculate_employee_expenses(self):
        total_employee_salary = 0
        for employee in self.employees:
            total_employee_salary += employee.salary
        return total_employee_salary

    def hire_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def fire_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            employee.surprise = None

    def give_surprise(self, employee, surprisable: Surprisable):
        if employee in self.employees:
            employee.surprise = surprisable