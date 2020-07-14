dict1 = {"orange":2, "banana":4, "apple":9}
print(type(dict1))
print(dict1.keys())
print(dict1.values())
dict1["mango"] = 5
print(dict1)
dict1["orange"] = 10
print(dict1)
dict2 = {"pinapple":14, "watermelon":1}
dict1.update(dict2)
print(dict1)
dict2.update(dict1)
print(dict2)
dict2.pop("watermelon")
print(dict2)