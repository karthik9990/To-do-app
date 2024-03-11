"""def prepare(text):
    text = text.title()
    text = text.strip()
    return text

print(prepare("hello    "))"""

'''def circle_ara(r):
    pi = 3.14
    area = 2*pi * r**2
    return area'''

"""
def speed(distance, time):
    return distance / time


print(speed(200, 4))


def get_area(x=10):
    return x * 2


area = get_area(x=1)
print(area)


def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)


import time
print(time.strftime("%A"))
"""

import random

lower_bound = int(input("Enter Lower_bound: "))
upper_bound = int(input("Enter Upper bound: "))

rand = random.randint(lower_bound,upper_bound)
print(rand)