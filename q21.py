# Program to check if a number is a palindrome

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num>0:
    reversed_num = reversed_num * 10 + num%10
    num = num // 10

if original_num==reversed_num:
    print("PALINDROME!!")
else:
    print("NOT PALINDROME!!")