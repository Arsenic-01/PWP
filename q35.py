# Write a Python function that takes a number as a parameter and check whether the number is prime or not.

def isPrime (num):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
            else:
                return True

print(isPrime(20))
