# Write a Python script to sort (ascending and descending) a dictionary by value.

d = {"1":"Apple","2":"Cherry","3":"Banana","4":"Dinosaur"}

sorted_asc = list(sorted(d.values()))
sorted_desc = list(sorted(d.values(), reverse=True))

print(sorted_asc)
print(sorted_desc)

