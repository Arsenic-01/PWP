# Write a Python program to find repeated elements from the Tuple.
# Input a tuple from User.

t = tuple()
n = int(input("Enter size of tuple: "))
for i in range(n):
    item = int(input("Enter element: "))
    t = t + (item,)

repeated = []
for i in range(len(t)):
    if t.count(t[i]) > 1 and t[i] not in repeated:
        repeated.append(t[i])

print("Tuple:", t)
print("Repeated elements:", repeated)
