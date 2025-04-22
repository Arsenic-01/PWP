# Program to print numbers in words from a tuple
# Input a tuple from user

t = tuple()
n = int(input("Enter size of tuple : "))

for i in range(n):
    num = int(input("Enter element : "))
    t += (num,)

digits = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

for number in t:
    print(number)
    
    for digit in str(number):
        print(digits[int(digit)], end=" ")
    print()
    