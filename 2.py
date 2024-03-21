import csv  # импортируем библиотеку для работы с csv файлами


with open('space.csv', encoding='utf-8') as file:  # открываем файл для чтения
    reader = list(csv.reader(file, delimiter='*'))[1:]  # заносим его строки в список
    b = []  # список с кодами корабля
    for ShipName, planet, coord_place, direction in reader:
        s = ShipName.split('-')
        b.append(int(s[1]))  # извлечение кода корабля из строки
    for i in range(len(b)-1):  # сортировка пузырьком по возрастанию
        for j in range(len(b)-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
    for i in range(10):  # первые десять кодов списка
        for ShipName, planet, coord_place, direction in reader:
            s = ShipName.split('-')
            if int(s[1]) == b[i]:
                print(ShipName)  # вывод полного имени корабля
