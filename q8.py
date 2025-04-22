# Write a Python program to Input elements in the Set and find out only Even Numbers from Set and Display it

s = set()

n = int(input("Enter the size of set : "))

for i in range(n):
    val = int(input("Enter element : "))
    s.add(val)
    
even = []

for i in s:
#    print(i)
    if i%2==0 and i not in even:
#        print("This Executed")
        even.append(i)

print(even)