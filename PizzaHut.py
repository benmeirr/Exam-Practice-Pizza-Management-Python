from datetime import datetime, timedelta
from overrides import overrides
from Pizza import Pizza


class PizzaHut(Pizza):

    def __init__(self, pizza_id, name, address, employees, phone_number):
        super().__init__(pizza_id, name, address, employees, phone_number)
        self.store_rank = self._calculate_rank()

    @overrides
    def _calculate_rank(self):
        total_employee_rank = 0
        for employee in self.employees:
            total_employee_rank += employee.rank
        average_rank = total_employee_rank / self.get_number_of_employees()
        return average_rank

    @overrides
    def calculate_ranged_rank(self, rank_range: int):
        if self.get_number_of_employees() > 0:
            current_date = datetime.now()
            validate_date = current_date - timedelta(days=rank_range)

            for employee in self.employees:
                if validate_date > employee.rank_date:
                    employee.set_rank()
            return self._calculate_rank()
        else:
            return 0
