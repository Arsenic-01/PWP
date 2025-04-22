# Write a Python program to select the even items of a list. Input a list from User

t = []
n = int(input("Enter size of list : "))

for i in range(n):
    val = int(input("Enter number : "))
    t.append(val)

even = []

for i in range(len(t)):
    print(t[i])
    if t[i]%2==0 and t[i] not in even:
        even.append(t[i])
        
print("Even no = ", even)
