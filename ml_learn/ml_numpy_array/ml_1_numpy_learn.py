import numpy as np 

mylist = [1,2,3,4,5]

myarr = np.array(mylist)
# print(type(myarr))

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
my_matrix_array = np.array(my_matrix)

# rows first, columns
myzeros = np.zeros((3,5))
# print(myzeros)

myones = np.ones((3,5))
# print(myones)

# linearly space, if you want to include endpoints, add 1 
mylinspace = np.linspace(0,10,11)
# print(mylinspace)
# print(len(mylinspace))

# square matrix , identity matrix
myidentitymatrix = np.eye(5)
# print(np.array2string(myidentitymatrix, separator=','))
# print(myidentitymatrix)

myr1 = np.random.rand(1)
# print(myr1)

myr2 = np.random.rand(5,10)
# print(myr2)

# standard normal distribution
myr3 = np.random.randn()
# print(myr3)

# random people age
myr4 = np.random.randint(0,101, (3,5))
# print(myr4)

# seed random state 
myr5 = np.random.seed(42)
myr6 = np.random.rand(4)
# print(myr6)

myr7 = np.arange(0,25)
# print(myr7)

# reformatted to rows x columns
myr8 = myr7.reshape(5,5)
# print(myr8)

# max, min ar

myr9 = np.random.randint(0,101, 10)
# print(myr9)
print(f'Max = {myr9.max()}, index location = {myr9.argmax()}\nMin = {myr9.min()}, datatype is {myr9.dtype}\nshape is {myr9.shape}')
myr9 = myr9.reshape(2,5)
print(myr9)
print(myr9.shape)
