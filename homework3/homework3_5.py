"""
Додати перевірку введеної IP-адреси. Адреса вважається коректно заданою, якщо вона:
складається з 4 чисел (а не літер чи інших символів)
числа розділені точкою
кожне число в діапазоні від 0 до 255 Якщо адреса неправильна, виводьте повідомлення: «Неправильна IP-адреса».
Повідомлення "Неправильна IP-адреса" має виводитися лише один раз, навіть якщо кілька пунктів вище не виконані.
"""

address = input("Enter your IP address: ").split(".")

if len(address) == 4:
    for element in address:
        if not element.isdigit() or int(element) > 255 or int(element) < 0:
            print("Wrong IP address")
            break
    else:
        print("IP address is correct")
else:
    print("Wrong IP address")
