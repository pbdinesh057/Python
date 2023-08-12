# args is a parameter that packs all arguments in a tuple
#useful when we wanna pass varying amount of arguments

#def add(*some_name)
#def add(*code)
#we can't change tuple's elements, instead we can convert the args(tuple) into a list.

#code = list(code)
def add(*args):
    # sum = num1 + num2
    # return sum
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,3,3,4,2,4,2))


#changing tuple elemets

def multiply(*stuff):
    mul=1
    stuff = list(stuff)
    stuff[0] = 10
    stuff[6] = 100
    for i in stuff:
        mul = mul*i
    return mul
print(multiply(1,2,3,4,2,1,3))