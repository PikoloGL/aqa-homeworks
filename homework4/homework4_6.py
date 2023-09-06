"""
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2 c,2 b,2 e,1 d,1 g,1 f,1
Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.
Use str.join() method and dict comprehension for print result
"""

input_string = input("Enter a string: ")
char_count = {}

for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1

output = ' '.join([f"{char},{count}" for char, count in char_count.items()])
print(output)
