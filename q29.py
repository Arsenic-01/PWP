# Write a Python program to combine two dictionary adding values for common Keys

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

common_dict = dict()

for key in d1:
    if key in d2:
        common_dict[key] = d1[key] + d2[key]
    else:
        common_dict[key] = d1[key]
        
for key in d2:
    if key not in common_dict:
        common_dict[key] = d2[key]
        
print("Combined dict with values added = ",common_dict)