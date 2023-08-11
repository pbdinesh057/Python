#Function is a block of code which is executed only when it's called

def hello():
    print("Hello")
    print("Have a Nice Day")
    print("\n")

for i in range(5):
    hello()


def name(name):
    print("Hello "+name)
my_name="Dinesh"
name(my_name)
#
def test(first,last,age):
    print("Hello "+first+" "+last)
    print("you are "+ str(age)+ " years old.")

fn=str(input("Enter First Name "))
ln=str(input("Enter Last name "))
old=int(input("Enter age "))
test(fn,ln,old)