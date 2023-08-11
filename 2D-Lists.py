# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a 2D list
print("Element at row 1, column 2:", matrix[0][1])  # Output: 2

# Iterating through a 2D list
print("Elements in the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# 1 2 3
# 4 5 6
# 7 8 9

# Modifying elements in a 2D list
matrix[1][2] = 99
print("Modified matrix:")
for row in matrix:
    print(row)

# Modified matrix:
# [1, 2, 3]
# [4, 5, 99]
# [7, 8, 9]

# Creating a 2D list with a list comprehension
rows = 3
columns = 4
matrix_comp = [[i * columns + j for j in range(columns)] for i in range(rows)]
print("Matrix with list comprehension:")
for row in matrix_comp:
    print(row)
