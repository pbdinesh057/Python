#A while loop in Python is used to repeatedly execute a block of code as long as a specified condition is True. The loop continues execution until the condition becomes False. Here's the general syntax of a while loop
count = 1
while count <= 5:
    print(count)
    count += 1
#User input with validation:
user_input = input("Enter a positive number: ")
while not user_input.isdigit():
    user_input = input("Invalid input. Enter a positive number: ")

number = int(user_input)
print(f"You entered: {number}")


#Sum of numbers:
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break  # Exit the loop if the user enters 0
    total += num

print(f"Sum of numbers: {total}")


#Printing a pattern:
rows = 5
current_row = 1
while current_row <= rows:
    print("*" * current_row)
    current_row += 1


#Using a while loop to create a menu:
while True:
    print("1. Play")
    print("2. High Scores")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Playing...")
    elif choice == "2":
        print("High scores...")
    elif choice == "3":
        print("Quitting...")
        break  # Exit the loop when user chooses to quit
    else:
        print("Invalid choice. Please choose again.")



#prompt 6 times to enter name and break
name = ""
count = 0
while len(name)==0:
    name = input("what's your name? ")
    count+=1
    if count==6:
        print("please enter name for next run")
        break

print("Hello " + name)

