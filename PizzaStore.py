from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from overrides import overrides
import Surprisable
from Rankable import Rankable


class PizzaStore(Rankable, ABC):
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

    @overrides
    def calculate_ranged_rank(self, rank_range: int):
        if self.get_number_of_employees() > 0:
            current_date = datetime.now()
            validate_date = current_date - timedelta(days=rank_range)

            for employee in self.employees:
                if validate_date > employee.pizza_rank_date:
                    employee.set_rank()
            return self.calculate_rank()
        else:
            return 0
