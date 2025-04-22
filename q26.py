# Write a Python program to find common items from two lists. Input a list from User

l1 = []
n = int(input("Enter no. of elements in list1 : "))

for i in range(n):
    val = int(input("Enter the element : "))
    l1.append(val)

l2 = []
n = int(input("Enter no. of elements in list2 : "))

for i2 in range(n):
    val = int(input("Enter the element : "))
    l2.append(val)
    

common_items = list(set(l1) & set(l2))

print("Common Items = ",common_items)