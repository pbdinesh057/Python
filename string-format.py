# optional method where it gives users more control when displaying outputs

animal = "cow"
item = "milk"
name = "Bro"
#positional arguments
print("The {} gives us {}".format(animal,item))

print("The {1} gives us {0}".format(item,animal))

print("The {} gives us {}".format(animal,item))

print("Hello, my name is {:10}.Nice to meet you".format(name)) #Hello, my name is Bro       .Nice to meet you

print("Hello, my name is {:<10}.Nice to meet you".format(name)) #Hello, my name is Bro       .Nice to meet you

print("Hello, my name is {:>10}.Nice to meet you".format(name)) #Hello, my name is        Bro.Nice to meet you

print("Hello, my name is {:^10}.Nice to meet you".format(name)) #Hello, my name is    Bro    .Nice to meet you

#numbers
number = 1000
print("The number of pi is {}".format(number)) #The number of pi is 1000
print("The number of pi is {:.3f}".format(number)) #The number of pi is 1000.000
print("The number of pi is {:,}".format(number)) #The number of pi is 1,000
print("The number of pi is {:b}".format(number)) #The number of pi is 1111101000
print("The number of pi is {:o}".format(number))#The number of pi is 1750
print("The number of pi is {:X}".format(number))#The number of pi is 3E8
print("The number of pi is {:E}".format(number))#The number of pi is 1.000000E+03
