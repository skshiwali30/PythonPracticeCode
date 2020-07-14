import numpy as np

l1 = [10, 20, 30, 40]
arr1 = np.array(l1)
print(type(arr1))

# initialise with 0 only
n2 = np.zeros((1,2))
print(n2)

# initialise with any specific no
n3 = np.full((3,3),23)
print(n3)

# initialise within range
n4 = np.arange(10,20)
print(n4)

# initialise within range with some interval
n5 = np.arange(10,30,5)
print(n5)

# to take any 5 random no in a range
n6 = np.random.randint(100,200,10)
print(n6)

# to know the shape of matrix
print(n6.shape)

# change shape of matrix
n6.shape = (10, 1)
print(n6)

# addition
# vertically
n7 = np.array([10, 20, 30])
n8 = np.array([40, 50, 60])
n9 = np.vstack((n7, n8))
print(n9)

# horizontally
n10 = np.hstack((n7, n8))
print(n10)

# column-wise
n11 = np.column_stack((n7, n8))
print(n11)

# numpy operation
n12 = np.array([10, 20, 30, 40, 50])
n13 = np.array([40, 20, 60, 70])

n14 = np.intersect1d(n12, n13)
print(n14)
n15 = np.setdiff1d(n12, n13)
print(n15)
n16 = np.setdiff1d(n13, n12)
print(n16)

# sum of all element
n17 = np.sum([n7, n8])
print(n17)

# addition column wise
n18 = np.sum([n7, n8], axis=0)
print(n18)

# addition row wise
n19 = np.sum([n7, n8], axis=1)
print(n19)

# basic increment in each element
r1 = np.array([10,12,45,78])
r1 = r1 + 1
print(r1)
r2 = r1 * 2
print(r2)
r3 = r1 - 1
print(r3)
r4 = r1 / 2
print(r4)

# math function - mean, median, standard deviation
print(np.mean(r1))
print(np.std(r1))
print(np.median(r1))

# numpy save n load
r2 = np.array([5, 10, 45, 16, 90])
np.save("my_numpy", r2)
r3 = np.load("my_numpy.npy")
print(r3)
