#used in functions , functions sends values/objects back to the caller. These values are knows as function's return values

def multiply(a,b):
    result = a*b
    return result

print(multiply(2,3))
a=multiply(6,8)
print(a)


def multiply(a,b):
    return a*b

print(multiply(5,6))
