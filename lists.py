fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry


numbers = [10, 20, 30, 40, 50]
length = len(numbers)
print(length)  # Output: 5

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

numbers = [1, 2, 3, 4, 5]
numbers[2] = 6
print(numbers)  # Output: [1, 2, 6, 4, 5]

fruits = ["apple", "banana", "cherry", "date"]
sliced_fruits = fruits[1:3]
print(sliced_fruits)  # Output: ['banana', 'cherry']


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Found banana!")


fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']


# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("List after appending elements:", my_list)

# Extending the list with another list
other_list = [40, 50]
my_list.extend(other_list)
print("List after extending with another list:", my_list)

# Inserting an element at a specific position
my_list.insert(2, 25)
print("List after inserting 25 at index 2:", my_list)

# Removing an element by value
my_list.remove(30)
print("List after removing 30:", my_list)

# Popping an element from a specific index
popped_element = my_list.pop(1)
print("Popped element:", popped_element)
print("List after popping element at index 1:", my_list)

# Clearing the list
my_list.clear()
print("List after clearing:", my_list)






# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Slicing
sliced_list = my_list[1:4]
print("Sliced list:", sliced_list)

# Counting occurrences of an element
count_20 = my_list.count(20)
print("Count of 20:", count_20)

# Finding index of an element
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# Copying a list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Combining lists
another_list = [60, 70]
combined_list = my_list + another_list
print("Combined list:", combined_list)

# List comprehension to filter elements
even_numbers = [x for x in my_list if x % 2 == 0]
print("Even numbers:", even_numbers)

# Original list: [10, 20, 30, 40, 50]
# First element: 10
# Last element: 50
# Sliced list: [20, 30, 40]
# Count of 20: 1
# Index of 30: 2
# Sorted list: [10, 20, 30, 40, 50]
# Reversed list: [50, 40, 30, 20, 10]
# Copied list: [50, 40, 30, 20, 10]
# Combined list: [50, 40, 30, 20, 10, 60, 70]
# Even numbers: [50, 40, 30, 20, 10]
