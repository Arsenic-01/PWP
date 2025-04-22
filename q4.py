# Write a Python program to display Even numbers from a tuple. Input a tuple from User.

t = tuple()

n = int(input("Enter size of tuple : "))

for i in range(n):
    val = int(input("Enter number : "))
    t += (val,)

even = []

for i in range(len(t)):
    print(t[i])
    if t[i]%2==0 and t[i] not in even:
        even.append(t[i])
        
print("Even no = ", even)
