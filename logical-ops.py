# and, or, not operators

# and: Returns True if both operands are True, otherwise, it returns False
x = 10
y = 5

result = (x > 5) and (y < 7)
print(result)  # Output: True

result = (x > 10) and (y < 7)
print(result)  # Output: False


# or: Returns True if at least one of the operands is True, otherwise, it returns False
x = 10
y = 5

result = (x > 5) or (y < 7)
print(result)  # Output: True

result = (x > 10) or (y < 7)
print(result)  # Output: True

result = (x > 10) or (y > 7)
print(result)  # Output: False


#not: Returns the opposite of the boolean value of the operand. If the operand is True, not will return False, and if the operand is False, not will return True.
x = 10
y = 5

result = not (x > 5)
print(result)  # Output: False

result = not (y > 7)
print(result)  # Output: True


#Logical operators are often used in if statements to create complex conditions. For example:
age = 25
income = 55000

if age >= 18 and income > 50000:
    print("You qualify for a loan")
else:
    print("You do not qualify for a loan")

