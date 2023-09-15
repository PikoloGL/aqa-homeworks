"""
Створіть декоратор, який виводить в консоль назву викликаної функції.
Наприклад, створіть пару функцій для арифметичних операцій підсумовування та множення.
Під час виклику цих функцій має бути повернутий результат операції,
а ім’я викликаної функції має відображатися на консолі разом із результатом.
Маленька підказка (__name__)
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func(*args, **kwargs))

    return wrapper


@my_decorator
def summ(num1, num2):
    return num1 + num2


@my_decorator
def multiply(num1, num2):
    return num1 * num2


number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
summ(number1, number2)
multiply(number1, number2)
