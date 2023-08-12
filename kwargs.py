#kwargs = Packs params into a dictionary
#useful so that a function can accept a varying no.of arguments

def hello(**kwargs):
    print("Hello", end = " ")
    for key,value in kwargs.items():
        print(value, end = " ")

hello(fn="Dinesh",ln="Pinnepalli",type="coder")