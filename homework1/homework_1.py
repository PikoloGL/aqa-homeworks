"""
Create variables john_salary and marta_salary of some type (floating point).
Assign the created variables the values you want.
Print the values of both variables to the console using the print method.
"""
john_salary = 100.55
marta_salary = 123.45

print(john_salary)
print(marta_salary)

"""
Create variables john_age and marta_age of integer type. 
Assign the created variables the values you want. 
Print the values of both variables to the console using the print method.
"""
john_age = 20
marta_age = 65

print(john_age, marta_age, sep="\n")

"""
Create string type variables john_name and marta_name. 
Assign the created variables the values you want. 
Print the values of both variables to the console using the print method.
"""
john_name = "John"
marta_name = "Marta"

print(john_name, marta_name, sep="\n")

"""
Create boolean variables john_gender and marta_gender. 
Let john be false and Marta be true. 
Print the values of both variables to the console using the print method.
"""
john_gender = False
marta_gender = True

print(john_gender, marta_gender, sep="\n")

"""
Create variables john_friends and marta_friends. 
Assign lists to variables. Each list must contain the names of friends. 
John has his list of friends and Martha has hers. Friends (friend's name) can be the usual strings "James", "Peter", etc
"""
john_friends = ["JohnJr", "JohnSr"]
marta_friends = ["Annie", "Clara", "Alice"]

print(john_friends, marta_friends, sep="\n")

"""
Create a list with people's names, some names should be repeated in it. 
Turn a list of duplicate names into a list of unique names using sets.
"""
name_list = ['John', 'John', 'Marta', 'Marta', 'Alex']

print(set(name_list))