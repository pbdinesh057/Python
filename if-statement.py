age = int(input("enter the age"))

if age==100:
    print("Centurion")
elif age>=18:
    print("Adult you are")
elif age<=0:
    print("not born yet")
else:
    print("you are a child")


#More Examples Below
# Example 1: Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else statement
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# Example 3: if-elif-else statement
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Below C")

# Example 4: Nested if statements
num = 25
if num % 2 == 0:
    if num % 5 == 0:
        print("Divisible by both 2 and 5")
    else:
        print("Divisible by 2 but not by 5")
else:
    print("Not divisible by 2")

# Example 5: Using logical operators in if statements
temperature = 28
if temperature > 30 and temperature <= 40:
    print("It's a hot day")
elif temperature > 40:
    print("It's a very hot day")
else:
    print("It's a moderate day")

# Example 6: Short-circuiting with logical operators
x = 10
y = 5
if x > 0 or y > 0:
    print("At least one of x or y is positive")

# Example 7: Ternary (conditional) operator
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)
