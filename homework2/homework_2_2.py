"""
Змішано V1 літрів води з температурою T1 та V2 літрів з температурою T2.
Написати програму, яка порахує об'єм і температуру суміші, що вийшла.
Обчислюється за формулою (v1 * t1 + v2 * t2) / (v1 + v2)
Всі параметри виводяться в консолі, вивести обʼєм та температуру
"""

volume1 = int(input("Volume of first part "))
temp1 = int(input("Temperature of first part "))
volume2 = int(input("Volume of second part "))
temp2 = int(input("Temperature of second part "))

mixture_volume = volume1 + volume2
mixture_temp = (volume1 * temp1 + volume2 * temp2) / mixture_volume

print("Mixture temperature: " + str(mixture_temp))
print("Mixture volume: " + str(mixture_volume))
