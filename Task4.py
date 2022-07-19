#Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)

import datetime
from random import random

def random_number():
    moment_date = datetime.datetimetoday()
    random = int(f"{moment_date.year}" + f"{moment_date.month}" + f'{moment_date.day}' + f'{moment_date.hour}' + f'{moment_date.microsecund}')
print(random)
