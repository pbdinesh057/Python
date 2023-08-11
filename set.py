#Sets are collections of unique elements, and they do not allow duplicate values. They are useful for tasks that involve checking for the presence of elements, finding intersections or differences between collections, and ensuring uniqueness of items.


# Creating a set
my_set = {10, 20, 30, 40, 50}
print("Set:", my_set)
# Output: Set: {10, 20, 30, 40, 50}

# Adding elements to a set
my_set.add(60)
my_set.add(70)
print("Set after adding elements:", my_set)
# Output: Set after adding elements: {70, 10, 20, 50, 60, 30, 40}

# Removing an element from a set
my_set.remove(30)
print("Set after removing 30:", my_set)
# Output: Set after removing 30: {70, 10, 20, 50, 60, 40}

# Checking membership in a set
is_present = 40 in my_set
print("Is 40 present in the set?", is_present)
# Output: Is 40 present in the set? True

# Union of sets
set1 = {10, 20, 30}
set2 = {20, 30, 40}
union_set = set1.union(set2)
print("Union of sets:", union_set)
# Output: Union of sets: {10, 20, 30, 40}

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)
# Output: Intersection of sets: {20, 30}

# Difference of sets
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)
# Output: Difference of sets: {10}

# Removing all elements from a set
my_set.clear()
print("Set after clearing:", my_set)
# Output: Set after clearing: set()

# Creating two sample sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Set 1:", set1)
print("Set 2:", set2)

# Adding elements to a set
set1.add(70)
print("Set 1 after adding 70:", set1)
# Output: Set 1 after adding 70: {70, 10, 20, 30, 40}

# Removing an element from a set
set2.remove(60)
print("Set 2 after removing 60:", set2)
# Output: Set 2 after removing 60: {40, 50, 30}

# Clearing a set
set1.clear()
print("Set 1 after clearing:", set1)
# Output: Set 1 after clearing: set()

# Union of sets
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)
# Output: Union of Set 1 and Set 2: {40, 50, 30}

# Difference of sets
difference_set = set2.difference(set1)
print("Difference of Set 2 and Set 1:", difference_set)
# Output: Difference of Set 2 and Set 1: {40, 50, 30}

# Updating a set with another set
set1.update(set2)
print("Set 1 after updating with Set 2:", set1)
# Output: Set 1 after updating with Set 2: {40, 50, 30}

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)
# Output: Intersection of Set 1 and Set 2: {40, 50, 30}
x
