# Write a Python program to multiplies all the items in a list. Input a list from User.

l = []
mul = 1

n = int(input("Enter no. of elements in list : "))

for i in range(n):
    val = int(input("Enter the element : "))
    l.append(val)
    
for i in range(n):
    mul *= l[i]
    
print(mul)