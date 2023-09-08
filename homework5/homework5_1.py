"""
Дано список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Лише за допомогою функцій map, lambda, zip
створити та надрукувати словник квадратів цих чисел.
Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# lambda
new_dict = {}
for val in str_list:
    val = int(val)
    square_val = lambda num: num ** 2
    new_dict[val] = square_val(val)
print(new_dict)

# zip
val_sqr = []
for val in str_list:
    val_sqr.append(int(val) ** 2)
new_zip_dict = dict(zip(map(int, str_list), val_sqr))
print(new_zip_dict)

# zip+map+lambda
print(dict(zip(map(int, str_list), map(lambda x: int(x) ** 2, str_list))))
