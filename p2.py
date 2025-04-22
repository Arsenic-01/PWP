import numpy as np

rand = np.random.randint(10,30,6)
print(rand)

ceff = [1,-3,9]
eq = np.poly1d(ceff)
print(eq)


mtx = np.array([[4,7],[6,9]])

det = np.linalg.det(mtx)
print(det)

inv = np.linalg.inv(mtx)
print(inv)
