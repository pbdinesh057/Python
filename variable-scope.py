#order of var scope

"""
Variable scope refers to where a variable is accessible and can be used within your code. Python has two main types of variable scope: global scope and local scope. Here's an explanation and examples of variable scope:

L = Local variable
E = Enclosing
G = Global
B = Built-in
"""

name = "Bro"
def display_name():
    name = "code" # Local scope variable, since it's defined inside the function
    print(name)

display_name() #calls Local var and print it
print(name) #Calls Global version of variable

# Global Scope
global_var = 10

def my_function():
    print("Inside my_function:", global_var)

my_function()
print("Outside my_function:", global_var)
# Output: Inside my_function: 10
#         Outside my_function: 10

################################################################################

# Local Scope
def my_function():
    local_var = 20
    print("Inside my_function:", local_var)

my_function()
# Error if trying to access local_var here

################################################################################

# Shadowing
x = 5

def shadow_example():
    x = 10
    print("Inside shadow_example:", x)

shadow_example()
print("Outside shadow_example:", x)
# Output: Inside shadow_example: 10
#         Outside shadow_example: 5

################################################################################

# Modifying Global Variables
global_var = 15

def modify_global():
    global global_var
    global_var = 25

modify_global()
print("Modified global_var:", global_var)
# Output: Modified global_var: 25

################################################################################

# Enclosing Scope (Closures)
def outer_function():
    x = 30
    def inner_function():
        print("Inside inner_function:", x)
    return inner_function

closure = outer_function()
closure()
# Output: Inside inner_function: 30

