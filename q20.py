#  Write a Python program to input a number and find the sum of digits in a number.

num = int(input("Enter a number : "))
sum_of_digits = 0

while num>0:
    sum_of_digits += num%10
    num = num // 10

print(sum_of_digits)