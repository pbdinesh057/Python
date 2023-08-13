import random

x = random.randint(1,1000)
y = random.random()
print(x)
print(y)


mylist = ["Rock","Paper","Scissors"]
Z = random.choice(mylist)
print(Z)

cards = [1,2,3,4,5,6,7,8,9,"A","Q","J","K"]
random.shuffle(cards)
print(cards)
S = random.choices(cards)
print(S)