# Write a Python program to generate a random float where the value is between 5 and 50 using the Python math module.

import math
import random

num = random.uniform(5,50)
num = math.floor(num * 100)/100
print(num)


n = random.randint(6,49)
print(n)