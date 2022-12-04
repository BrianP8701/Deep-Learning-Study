import numpy as np 

a = np.array([1, 2, 4])

b = np.array([[1, 2, 3],
             [4, 5, 6], 
             [7, 8, 9]], dtype = float)

c = 3*np.ones(shape = (8,3))

d = np.linspace(0, 10, 11)  

e = np.arange(3,100,10)

f = range(0, 35, 5) # Same as arange

for i in f:
    x = 5

g = np.eye(10, 10, 5, float, 'F')

h = np.empty((3, 3), float)

i = np.array([('Rocky', 5, 13.2), ('Romeo', 8, 11.2), ('Troy', 6, 9.7)],
             dtype=[('name', 'U10'), ('strength', 'i4'), ('cuteness', 'f4')])

j = np.random.random((3, 3))

k = np.array([[1, 2, 3, 7],
             [4, 5, 6, 7], 
             [7, 8, 9, 7]], dtype = float)

l = np.array([[1, 2, 3, 4],
             [5, 6, 7, 8]],
             dtype = float)
m = np.array([[1, 2],
             [3, 4], 
             [5, 6],
             [7, 8]],
             dtype = float)
np.matmul(l, m)
n = np.ones((4, 2, 3))
o = np.zeros((5, 2, 3))

print(np.concatenate((n, o)))