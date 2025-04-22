# Input two Sets from User and find the common elements between them without using any inbuilt function.

s1 = set()
s2 = set()

n = int(input("Enter the size of set 1 : "))

for i in range(n):
    val = int(input("Enter element : "))
    s1.add(val)

n = int(input("Enter the size of set 2 : "))

for i in range(n):
    val = int(input("Enter element : "))
    s2.add(val)
    
common_elements = []

for item in s1:
    if item in s2:
        common_elements.append(item)

print(common_elements)

