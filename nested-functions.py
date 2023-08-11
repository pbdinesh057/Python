# Nested Function calls
#Function calls inside other function calls
#innermost functions are resolved first
#returned value is used as argument for next outer function

def outer_function():
    x = 10

    def inner_function():
        y = 5
        result = x + y
        return result

    return inner_function()

print(outer_function())
# Output: 15




def power_function(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

square = power_function(2)
cube = power_function(3)

print(square(4))
# Output: 16

print(cube(3))
# Output: 27


