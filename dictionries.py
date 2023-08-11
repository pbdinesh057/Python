#A dictionary in Python is a collection of key-value pairs where each key is associated with a value. Dictionaries are unordered, mutable, and can contain various types of data. Here's a concept overview along with some examples:
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(student)
# Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

# Accessing values using keys
name = student["name"]
age = student["age"]
print("Name:", name)
print("Age:", age)
# Output: Name: Alice
#         Age: 20

# Modifying values
student["age"] = 21
print("Modified Dictionary:", student)
# Output: Modified Dictionary: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# Adding a new key-value pair
student["gender"] = "Female"
print("Dictionary with New Pair:", student)
# Output: Dictionary with New Pair: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'gender': 'Female'}

# Removing a key-value pair
del student["age"]
print("Dictionary after Deletion:", student)
# Output: Dictionary after Deletion: {'name': 'Alice', 'major': 'Computer Science', 'gender': 'Female'}

# Iterating through keys
for key in student:
    print(key, ":", student[key])
# Output: name : Alice
#         major : Computer Science
#         gender : Female

# Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)
# Output: Keys: dict_keys(['name', 'major', 'gender'])
#         Values: dict_values(['Alice', 'Computer Science', 'Female'])
#         Items: dict_items([('name', 'Alice'), ('major', 'Computer Science'), ('gender', 'Female')])



capitals = {'USA':'WashinhtonDC',
            'India':'New Delhi',
            'Russia': 'Moscow',
            'China': 'Beijing'}

print(capitals['Russia'])

for i in capitals:
    print(i+":"+"\t"+capitals[i])

print(capitals.get('Pak'))
print(capitals.values())
print(capitals.keys())


# for keys,values in capitals.items():
#     print(key, values)