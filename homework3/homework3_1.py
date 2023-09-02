"""
Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
"""

word = input("Enter your word: ")

if word == word[::-1]:
    print("+")
else:
    print("-")
