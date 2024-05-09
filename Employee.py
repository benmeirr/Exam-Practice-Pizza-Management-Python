import random
from datetime import datetime


class Employee:

    def __init__(self, employee_id, first_name, last_name, address, salary, start_date, pizza_rank, pizza_rank_date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.salary = salary
        self.start_date = start_date
        self.pizza_rank = pizza_rank
        self.pizza_rank_date = pizza_rank_date
        self.surprise = None

    def set_rank(self):
        self.pizza_rank = random.randint(0, 100)
        self.pizza_rank_date = datetime.now()
