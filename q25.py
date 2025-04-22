# Write a Python program to reverse a list. Input a list from User.

l = []
n = int(input("Enter no. of elements in list : "))

for i in range(n):
    val = int(input("Enter the element : "))
    l.append(val)
    
l.reverse()
    
print("List Reverse = ",l)