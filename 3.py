import csv  # импортируем библиотеку для работы с csv файлами


with open('space.csv', encoding='utf-8') as file:  # открываем файл для чтения
    reader = list(csv.DictReader(file, delimiter='*', quotechar='"'))  # заносим его строки в список из словарей

namekor = input()  # вводи искомое имя
while namekor != 'stop':  # если не стоп команда
    for row in reader:
        if row['ShipName'] == namekor:  # ищем имя в строках, если совпадает
            print(f"Корабль {row['ShipName']} был отправлен с планеты: {row['planet']} и его направление движения было: {row['direction']}")
            break
    else:  # иначе
        print("error.. er.. ror..")  # ошибка
    namekor = input()  # продолжаем искать
