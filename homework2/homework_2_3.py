"""
Написать калькулятор с основными операциями(+, -, *, /)
Користувач вводить два числа та арифметичну операцію
Також можна додати перевірку для всіх задач з негативним сценарієм
"""

number1 = int(input("First number:"))
operator = input("Operator:")
number2 = int(input("Second number:"))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    if number2 == 0:
        print("You cant divide by 0")
    else:
        print(number1/number2)
elif operator == "**":
    print(number1 ** number2)
elif operator == "%":
    print(number1 % number2)
elif operator == "//":
    print(number1 // number2)
