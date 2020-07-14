import numpy as np
from matplotlib import pyplot as pt

# Line plot on windows
x = np.arange(2,20)
y = x * 2
print(x)
print(y)

pt.plot(x,y)
pt.xlabel("x-axis")
pt.ylabel("y-axis")
pt.title("x-y graph")
pt.show()

pt.plot(x, y, color="red", linestyle="--", linewidth=4)
pt.show()

y1 = x * 3
pt.plot(x, y1, color="blue", linestyle=":", linewidth=4)
pt.grid(True)
pt.show()

# two line plot on same window
pt.subplot(1,2,1)
pt.plot(x, y, color="blue", linestyle=":", linewidth=4)
pt.subplot(1,2,2)
pt.plot(x, y1, color="green", linestyle="--", linewidth=4)
pt.show()

# Bar plot on windows
student = {'Bob':24, 'Amit':37, 'mehar':23, 'uma':45}
names = list(student.keys())
values = list(student.values())

pt.bar(names, values)
pt.xlabel("x-axis")
pt.ylabel("y-axis")
pt.title("x-y bar graph")
pt.show()

# scatter graph
n1 = [1,2,3,4,5,6,7,8]
n2 = [8,7,6,5,4,3,2,1]
# pt.scatter(n1, n2)
pt.scatter(n1, n2, marker = "*", c="g", s= 30)
pt.show()

# Histogram
n3 = [1,2,2,4,4,4,5,6,7,8,8,8,8,9,9,1,2,3,2,2,2,3]
pt.hist(n3)
pt.show()

# Pie-chart
n4 = ["cooking", "eating", "sleeping", "reading", "learning"]
n5 = [50, 25, 15, 9, 1]
pt.pie(n5, labels=n4)
pt.show()

# Dough-nut chart
pt.pie(n5, labels=n4, radius = 2)
pt.pie([1], colors="w", radius = 1)
pt.show()