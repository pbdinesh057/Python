student = ("Bro",21,"male")
print(student.count("Bro"))
print(student.index("male"))

for i in student:
    print(i)

if "Bro" in student:
    print("Bro is here")

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple) #Tuple: (10, 20, 30, 40, 50)

# Accessing elements in a tuple
first_element = my_tuple[0]
last_element = my_tuple[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Slicing a tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple:", sliced_tuple) #Sliced tuple: (20, 30, 40)

# Counting occurrences of an element in a tuple
count_20 = my_tuple.count(20)
print("Count of 20:", count_20)

# Finding index of an element in a tuple
index_30 = my_tuple.index(30)
print("Index of 30:", index_30)

# Converting a tuple to a list
tuple_to_list = list(my_tuple)
print("Tuple converted to list:", tuple_to_list) #Tuple converted to list: [10, 20, 30, 40, 50]

# Concatenating tuples
another_tuple = (60, 70)
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple) #Combined tuple: (10, 20, 30, 40, 50, 60, 70)
