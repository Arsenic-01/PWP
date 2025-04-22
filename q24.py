# Write a Python program to get the largest number and smallest number from a list. Input a list from User.

l = []
n = int(input("Enter no. of elements in list : "))

for i in range(n):
    val = int(input("Enter the element : "))
    l.append(val)
    
print("Largest no = ",max(l))
print("Smallest no = ",min(l))
