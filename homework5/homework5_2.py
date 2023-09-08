"""
Напишіть інтерактивний калькулятор.
Передбачається, що користувач вводить формулу, що складається з числа, оператора (як мінімум * і /) та іншого числа,
розділених пробілом (наприклад, 2 * 5).
Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
Якщо введені числа не можуть бути float спіймайте ValueError
Також ловіть помилку при діленні на 0
В кожній спійманій помилці друкуйте пояснення, що пішло не так
За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором,
якщо введені не вірні дані
Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
Результат виконання формули - float число з двома знаками після крапки
"""


class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


counter = 3
while counter != 0:
    try:
        formula = input("Enter your formula with two values and one operator separated with spaces(as example: 2 * 5): ")
        elements = formula.split()

        if len(elements) != 3:
            raise FormulaError

        num1 = int(elements[0])
        operator = elements[1]
        num2 = int(elements[2])

        if operator not in ("/", "*"):
            raise WrongOperatorError
        elif operator == "/" and num2 == 0:
            raise ZeroDivisionError
        elif num1 is float or num2 is float:
            raise ValueError
        elif operator == "*":
            result = num1 * num2
            print(float('{:.2f}'.format(result)))
            break
        elif operator == "/":
            result = num1 / num2
            print(float('{:.2f}'.format(result)))
            break
        elif counter == 0:
            print("You wasted all tries!")
    except FormulaError:
        print("Incorrect input format")
        counter -= 1
    except WrongOperatorError:
        print("You should use only * or / as operators.")
        counter -= 1
    except ValueError:
        print("You can`t enter float numbers.")
        counter -= 1
    except ZeroDivisionError:
        print("You can`t divide by 0.")
        counter -= 1
    else:
        print("Execution successful!")
    finally:
        if counter > 0:
            print(f"Only {counter} tries left")
        else:
            print("Sorry no tries left.")
