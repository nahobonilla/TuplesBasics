fruit_tuple = ("apple", "banana", "cherry", "date")
print("First element:", fruit_tuple[0])
print("Last element:", fruit_tuple[-1])
slice_tuple = fruit_tuple[1:3]
print("Slice tuple:", slice_tuple)

num_tuple = (3, 5, 3, 2, 8, 3, 7)
count_3 = num_tuple.count(3)
index_8 = num_tuple.index(8)
print("Count of 3:", count_3)
print("index of 8" , index_8)

person_info = ("Alice", 28, "Engineer")
name, age, profession = person_info
print("Name:",  name)
print("Age:", age)
print("Profession:",  profession)