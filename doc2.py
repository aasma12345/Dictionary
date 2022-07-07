# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}






string = input("Enter a string: ")
dict = {}
for char in string:
    if char in dict: 
        dict[char]=dict[char]+1
    else:
        dict[char]=1 
for key in dict:
    print(key,':',dict[key])




