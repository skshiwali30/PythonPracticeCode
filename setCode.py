set1 = {1, 45, "sparta", 7.8, "kavya", 1, 7, 7.8}
print(set1)
set1.add("anshu")
print(set1)
set1.update((10,20,20,"alien"))
print(set1)
set1.remove(20)
print(set1)
set2 = {3, 6, 7, "kavya", 90}
print(set1.union(set2))
print(set1.intersection(set2))