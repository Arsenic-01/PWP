# Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters.

def calc_case(st):
    lc = 0
    uc = 0
    
    for i in st:
        if i.isupper():
            uc+=1
        elif i.islower():
            lc+=1
    
    return [lc,uc]

l = calc_case("IdkBroHaHa")

print("Lower Case = ",l[0])
print("Upper Case = ",l[1])

print(type(l))