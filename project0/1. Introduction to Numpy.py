import numpy as np
x = [1, 5]
# x+1 not possible

x = np.array(x)
print(x)
print(x+1)
print(x+2)
print(x-4)
print(x*5)
y = np.array([5, 6])
print(x+y)
print(x*y)
print(x/y)
print(np.zeros([4,5]))
print(np.ones([4,5]))
print(np.random.random([2, 3]))



#Matrix properties and operations
x = np.array([3,5])
print(x)
x.shape #tells dimension of matrix
y=np.array([[3, 5, 1], [1, 3, 9]])
print(y)
y.shape

z = y.transpose() #transpose of matrix
print(z)
z.shape

z = y+3
z*y #element wise multiplication
np.matmul(x, z) #cross multiplication

print(x)
print(np.exp(x))
print(np.sin(x))
print(np.cos(x))
print(np.tanh(x))



#Max, Min, Norm
x=np.array([4, 2, 9, -6, 5, 11, 3])
print("\n\n")
print(x)
print(np.max(x))
print(x.max()) #Same as above line
print(np.min(x))
print(x.min())

print(np.linalg.norm(x)) #squareroot of sum of squares in x

#np.vectorize(my_func)
#to vectorize a function