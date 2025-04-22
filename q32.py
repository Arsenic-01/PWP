# Python Program to input values from the user in a dictionary where keys will be automatically generated using range.

n = int(input("Enter the size of dict : "))
d = dict()
for i in range(n):
    val = int(input("Enter element value : "))
    d[i] = val

print(d)