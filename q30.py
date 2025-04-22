# Write a Python program to print all unique values in a dictionary.

d1 = {"a":100, "b":200, "c":300, "d":400, "e":100, "f":200}
uniq_d = []

for value in d1.values():
    if value not in uniq_d:
        uniq_d.append(value)

print(uniq_d)