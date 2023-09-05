"""
 У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
 перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]
"""

variables = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_variables = []

for var in variables:
    snake_case = ''
    prev_char = ''
    for char in var:
        if char.isupper() and prev_char.isalpha():
            snake_case += '_' + char.lower()
        else:
            snake_case += char.lower()
        prev_char = char
    snake_case_variables.append(snake_case)

print(snake_case_variables)
