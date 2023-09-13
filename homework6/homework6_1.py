"""
Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну дату
(курс задається окремою змінною).
Результат зберегти новий файл salaries_uah.csv
"""
import csv

exchange_rate = 40

with open('test_file.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    data = list(csv_reader)

for row in data[1:]:
    for i in range(1, len(row)):
        row[i] = str(int(row[i]) * exchange_rate)

with open('salaries_uah.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(data)

