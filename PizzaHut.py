from overrides import overrides
from PizzaStore import PizzaStore


class PizzaStoreHut(PizzaStore):

    def __init__(self, pizza_id, name, address, employees, phone_number):
        super().__init__(pizza_id, name, address, employees, phone_number)
        self.store_rank = self.calculate_rank()

    @overrides
    def calculate_rank(self):
        total_employee_rank = 0
        for employee in self.employees:
            total_employee_rank += employee.pizza_rank
        average_rank = total_employee_rank / self.get_number_of_employees()
        return average_rank
