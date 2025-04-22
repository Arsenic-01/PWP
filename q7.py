# Write a Python program to find maximum and the minimum value in a set and to find the length of a set.

s = set()

n = int(input("Enter the size of set : "))

for i in range(n):
    val = int(input("Enter element : "))
    s.add(val)

print("Set = ",s)
print("Max value in set = ",max(s))
print("Min value in set = ",min(s))
print("Length of set = ",len(s))