"""
Написати програму, яка вміє переводити температуру з C в Фаренгейти і Кельвіни
Наприклад: дана температура в Цельсіях 25 С
Фаренгейт: 45.9F - вважається за формулою C * 9/5 + 32
Кельвіни: 298.16K - вважається за формулою C + 273.15
Користувач вводить температуру в градусах Цельсіях, програма выводить температуру в Фаренгейтах та Кельвінах
"""

temp_celsius = int(input("Enter the temperature that needed to be converted "))

temp_fahrenheit = temp_celsius * 9/5 + 32
temp_kelvin = temp_celsius + 273.15

print("Here is temperature converted into fahrenheit: " + str(temp_fahrenheit) + " F")
print("Here is temperature converted into kelvin: " + str(temp_kelvin) + " K")
