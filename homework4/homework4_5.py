"""
The list of names is given: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
Using the continue statement, print only the correct names to the console
"""

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names:
    if isinstance(name, str):
        print(name)
    else:
        continue
