# Exception handling in Python allows you to gracefully handle errors that may occur during program execution.
# It helps prevent your program from crashing and provides a way to handle unexpected situations

try:
    # The 'try' block encloses code that may raise an exception
    numerator = int(input("Enter the Numerator: "))  # Accept user input for the numerator
    denominator = int(input("Enter the Denominator: "))  # Accept user input for the denominator
    result = numerator / denominator  # Perform division

except ZeroDivisionError as e:
    # 'except' block for handling the ZeroDivisionError exception
    print(e)  # Print the exception message
    print("Can't be divided by 0!!")  # Custom message for ZeroDivisionError
except ValueError as e:
    # 'except' block for handling the ValueError exception
    print(e)  # Print the exception message
    print("Enter only numbers!")  # Custom message for ValueError
except Exception as e:
    # 'except' block for handling other exceptions
    print(e)  # Print the exception message
    print("Something went wrong")  # Custom message for other exceptions
else:
    # The 'else' block is executed if no exception occurs
    print(result)  # Print the result of the division

finally:
    # The 'finally' block is always executed, regardless of whether an exception occurred or not
    print("This code is always executed")
