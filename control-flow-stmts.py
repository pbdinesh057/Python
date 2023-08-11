# break:
# break is used to immediately exit (terminate) the innermost loop or the current iteration of a loop.
# It is often used to exit a loop prematurely when a certain condition is met.
# After break is encountered, the program execution continues after the loop.


for i in range(10):
    if i == 5:
        break
    print(i)

# continue:
# continue is used to skip the rest of the current iteration of a loop and move to the next iteration.
# It is often used when you want to skip certain values or cases within a loop.

for i in range(6):
    if i == 3:
        continue
    print(i)

#
# pass:
# pass is a placeholder statement that does nothing. It's often used as a placeholder when you need a statement for syntactical reasons but you don't want to execute any code.
# It can be useful for writing a stub for a function or a loop that you intend to implement later.

for i in range(10):
    if i==5:
        pass
    else:
        print(i)
# Placeholder, doesn't do anything yet\



phone="628-141-25_5"
for i in phone:
    if i =="-":
        pass
    else:
        print(i, end="")
print("\n")


phone="628-141-2575"
for i in phone:
    if i =="-":
        continue
    else:
        print(i, end="")