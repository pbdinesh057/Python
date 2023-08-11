import time
import math


for i in range(10,15):
    print(i)

for i in range(0,50,2):
    print(i)

for i in "Dinesh":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")


## NESTED LOOPS (One Loop inside an other loop


rows=int(input("How many ROWS: "))
columns=int(input("How many Columns: "))
symbol=input("enter the symbol or pattern instance: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ") #The end=" " argument in the print() function ensures that the symbols are printed on the                          same line with a space separator.
    print() # statement after the inner loop moves to the next line after printing a full row


for i in range(5):
    print(i, end=" ")
print("\n")


names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name, end=" | ")


#Printing a Multiplication Table:

for i in range(1,11):
    for j in range(1,11):
        print(i * j, end="\t")
    print()


for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

#prime numbers in a range
Lower=int(input("Lower Limit: "))
Upper=int(input("Upper Limit: "))

for i in range(Lower,Upper+1):
    if i>1:
        for j in range(2, int(i**0.5)+1):
            if i % j ==0:
                break
        else:
            print(i, end=" ")
Lower=int(input("Lower Limit: "))
Upper=int(input("Upper Limit: "))
# num_list=[]
prime_list=[]
# for num in range(Lower, Upper+1):
#     num_list.append(num)
# print(num_list)

for i in (Lower, Upper+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
        if count==2:
            prime_list.append(i)
print(prime_list)



# a=9
# b=a/2
# print(math.floor(b))




