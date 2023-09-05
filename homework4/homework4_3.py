"""
Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
Виведіть по черзі для усіх елементів словника повідомлення типу
My favorite programming language is Python. It was created by Guido van Rossum.
Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
Виведіть словник на екран.
"""

programming_languages = {
    "Java": "James Gosling",
    "Python": "Guido van Rossum",
    "C++": "Bjarne Stroustrup",
    "C#": "Eric Lippert"}

for language, developer in programming_languages.items():
    print(f"My favourite programming language is {language}. It was created by {developer}")

del programming_languages["Python"]
print(programming_languages)
