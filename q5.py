# Write a Python program to create a set, add member(s) in a set and remove one item from set.

s = set()
n = int(input("Enter size of set : "))

for i in range(n):
    val = int(input("Enter element : "))
    s.add(val)

print(s)

uval = int(input("Enter the element that you want to remove : "))

try:
    s.remove(uval)
except Exception:
    print("Enter an element that exists in the set!")
    
print(s)