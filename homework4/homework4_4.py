"""
You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
Names of people in the format "John Dow" first and second name.
Find those who are on all blacklists.
"""

casino_blacklist = [
    "Albert Einstein",
    "Marie Curie",
    "Nikola Tesla",
    "Ada Lovelace",
    "Leonardo da Vinci",
    "Frida Kahlo"
]
poker_blacklist = [
    "Marie Curie",
    "Nikola Tesla",
    "Harry Potter",
    "Leonardo da Vinci",
    "Frida Kahlo"
]
alcohol_blacklist = [
    "Beyoncé Knowles",
    "Leonardo da Vinci",
    "Sherlock Holmes",
    "Frida Kahlo",
    "Isaac Newton"
]

all_blacklist = []
for name in casino_blacklist:
    if name in poker_blacklist and name in alcohol_blacklist:
        all_blacklist.append(name)
print(all_blacklist)
