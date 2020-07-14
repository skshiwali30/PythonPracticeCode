g = lambda x : x*x*x
print(g(5))

# lambda with filter - wants some particular elements among all
l1 = [17, 10, 50, 55, 34, 80]
l2 = list(filter(lambda x :(x%2 == 0),l1))
print(l2)

# lambda with map - perform operation on all items of list
l3 = list(map(lambda x : x*2,l1))
print(l3)

# lambda with reduce - provide consolidate values of list
from functools import reduce
l4 = reduce(lambda x,y : x+y, l1)
print(l4)
