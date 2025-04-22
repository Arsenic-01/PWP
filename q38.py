# Write a Python program with the user defined function which accepts a number & returns Fibonacci series of given numbers

def fib(num):
    l = []
    a,b = 0,1
    while (num>0):
        l.append(a)
        a,b = b,a+b
        num-=1
    return l

print(fib(10))