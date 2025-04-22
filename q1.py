# Write a Python program to find sum of all elements, largest element and smallest element from the Tuple.
# Input a tuple from User.

t = tuple()
n = int(input("Enter size of tuple : "))
for i in range(n):
    item = int(input("Enter element : "))
    t = t + (item,)

print(t)
print("Sum of elements = ",sum(t))
print("largest element = ",max(t))
print("smallest element = ",min(t))
