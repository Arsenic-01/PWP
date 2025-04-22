# Write a Python program to check if the input number is prime or not.

def isPrime(num):
    flag = 0
    for i in range(2,int(((num/2)+1))):
        print(i)
        if num%i == 0:
            flag = 1
            break
    if flag==0:
        print(num," is a Prime number")
    else:
        print(num," is NOT a Prime number")

num1 = int(input("Enter a number : "))
isPrime(num1)