import pandas as pd

print("------------------------- Series ------------------------------")
p1 = pd.Series([10, 20, 40, 30])
print(p1)
print(type(p1))

# change the index
p2 = pd.Series([10, 20, 40, 30], index = [0, 'b', 'c', 'd'])
print(p2)
print(type(p2))

#  series as dict
p3 = pd.Series({"a":89, "b":23, "c":67 })
print(p3)

p4 = pd.Series({"a":89, "b":23, "c":67 }, index = ["c", 2, "b", "a"])
print(p4)

p5 = pd.Series([1,4,2,7,5,9,3])
print(p5[1])
print(p5[:6])
print(p5[4:])
print(p5[-3:])

# basic operation on scaler value to every element
p6 = p5 + 2
print(p6)
print(p5 - 10)
print(p5 * 10)
print(p5 / 10)

print("Sum of two series object =\n",p6 + p5)

print("-------------------------------------- Data-Frame ------------------------------")

d1 = pd.DataFrame({"Name":["Shiwali", "Anshu", "Sony"], "Marks":[97, 95, 93]})
print(d1)




