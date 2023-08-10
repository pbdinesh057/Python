text = "Hello, world!"

# Basic slicing
print(text[0:5])   # Output: "Hello"
print(text[7:12])  # Output: "world"
print(text[::1])   # Output: "Hello, world!"

# Omitting start or end index
print(text[:5])    # Output: "Hello" (from the beginning to index 5 - 1)
print(text[7:])    # Output: "world!" (from index 7 to the end)

# Negative indices (counting from the end)
print(text[-6:-1]) # Output: "world" (from the 6th character from the end to 1 character from the end)

# Using step (stride)
print(text[0:12:2])    # Output: "Hlo o" (every second character from index 0 to 12 - 1)
print(text[::-1])      # Output: "!dlrow ,olleH" (reverses the string)


###         SLICING           ###

web1 = "https://google.com"
web2 = "https://wikepedia.com"
a = slice(8,-4)
print(web1[a])
print(web2[a])

# Slicing with variables
start = 2
end = 8
print(text[start:end])  # Output: "llo, w" (using variables to define the slice)

# Slicing inside functions
def get_middle(s):
    return s[len(s)//2-1:len(s)//2+1]

print(get_middle("Python"))  # Output: "th"
