# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial (num):
    fac = 1
    for i in range(1, num+1):
        fac *= i
    
    return fac

print(factorial(5))