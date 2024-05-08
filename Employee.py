import random
from datetime import datetime


import Surprisable


class Employee:

    def __init__(self, employee_id, first_name, last_name, address, salary, rank, rank_date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.salary = salary
        self.rank = rank
        self.rank_date = rank_date
        self.__surprise = None

    def set_rank(self):
        self.rank = random.randint(0,100)
        self.rank_date = datetime.now()

    @property
    def surprise(self):
        return self.__surprise

    @surprise.setter
    def surprise(self, surprise: Surprisable):
        self.__surprise = surprise

