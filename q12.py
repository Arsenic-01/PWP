# Write a Python program to check if the input year is a leap year of not.

year = int(input("Enter a year : "))
isLeap = False

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
    isLeap = True
    
if isLeap:
    print(year," is a Leap year")
else:
    print(year," is NOT a Leap year")
