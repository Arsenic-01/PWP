# Write a Python program to find the highest 3 values in a dictionary.

d1 = {"a": 100, "b": 200, "c": 300, "d": 400, "e": 150, "f": 250}

sorted_val = sorted(d1.values(), reverse=True)[:3]

print(sorted_val)