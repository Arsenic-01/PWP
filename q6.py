# Write a Python program to perform following operations on set: intersection of sets, union of sets, set
# difference, symmetric difference, clear a set.

s1 = set()
s2 = set()

s1 = {10,20,30,40}
s2 = {10,20,50,60}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

s1.clear()
s2.clear()

print(s1,s2)