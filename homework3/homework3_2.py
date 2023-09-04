"""
Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'
"""

sentence = input("Enter your sentence: ")
word = input("Enter your word: ")

# Через класичний if-else:
if word in sentence:
    print("YES")
else:
    print("NO")

# Через тернарний оператор:
result = print("YES") if word in sentence else print("NO")
