"""
Користувач вводить текст через пробіл.
Конвертувати текст у список.
Вивести останні 3 елементи зі списку, якщо список містить менше 3-х елементів,
вивести повідомлення про те що кількість елементів менша за 3 і вказати кількість елементів поточного списку
"""

text = list(input("Enter your text: "))

if len(text) > 3:
    print(text[-3:])
else:
    print(f"There are less than 3 elements in list. Current list have {len(text)} elements")
