"""
Напишіть функцію з такою сигнатурою: def display_box(width: int, height: int, character="*") .
Ця функція намалює простий прямокутник заданої висоти та ширини, використовуючи character для друку ліній.
Наприклад, display_box(5, 4, 'x') має вивести наступне:

xxxxx

x      x

x      x

xxxxx
"""


def display_box(width: int, height: int, character="*"):
    if width <= 0 or height <= 0:
        print("Incorrect input data.")
        return
    else:
        print(width * character)
        for element in range(height - 2):
            print(character + " " * (width - 2) + character)
        if height > 1:
            print(character * width)
        return


if __name__ == "__main__":
    width_input = int(input("Enter your width: "))
    height_input = int(input("Enter your height: "))
    print(display_box(width=width_input, height=height_input))
