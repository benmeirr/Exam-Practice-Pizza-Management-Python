from datetime import datetime, timedelta

from BacketBall import BasketBall
from Employee import Employee
from PizzaDominos import PizzaDominos
from PizzaHut import PizzaHut

if __name__ == "__main__":

    # create employees
    employee_1 = Employee(1, "John", "Doe", "123 street", 300, 50, datetime.now())
    employee_2 = Employee(2, "Jane", "Doe", "456 street", 350, 70, datetime.now())
    employee_3 = Employee(3, "James", "Doe", "789 street", 400, 80, datetime.now())

    # create pizza shops
    pizza_dominos = PizzaDominos("PD001", "Dominos", "1000 street", [employee_1, employee_2], "+123456")
    pizza_hut = PizzaHut("PH001", "Pizza Hut", "2000 street", [employee_3], "+789101")

    # hire new employee
    employee_4 = Employee(4, "Jake", "Doe", "1000 street", 500, 90, datetime.now())
    pizza_dominos.hire_employee(employee_4)
    # check number of employees
    print(pizza_dominos.get_number_of_employees()) # should print 3

    # calculate and print expenses
    print(pizza_dominos.calculate_employee_expenses()) # should print 1150

    # set surprise for an employee
    surprise_1 = BasketBall()
    pizza_dominos.give_surprise(employee_4, surprise_1)
    employee_4.surprise.activate_surprise() # should print "You got a surprise! Congratulations!"

    # fire an employee
    pizza_dominos.fire_employee(employee_4)
    print(pizza_dominos.get_number_of_employees()) # should print 2
    print(employee_4.surprise) # should be None

    # set the rank dates for each employee
    employee_1.rank_date = datetime.now() - timedelta(days=10)
    employee_1.rank = 10
    employee_2.rank_date = datetime.now() - timedelta(days=5)
    employee_2.rank = 10

    # calculate and print the ranged rank for the last 7 days for each pizzeria
    print(pizza_dominos.calculate_ranged_rank(7))
    print(f'rank: {employee_1.rank}, rank date: {employee_1.rank_date}')
    print(f'rank: {employee_2.rank}, rank date: {employee_2.rank_date}') ## only employee 2 should print the original rank and rank date



