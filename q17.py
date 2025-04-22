# Write a Python program to print Fibonacci series.

n = int(input("Enter the no. of term you want to generate : "))

a,b = 0,1

for i in range(n):
    print(a, end=" ")
    a,b = b, a+b
    