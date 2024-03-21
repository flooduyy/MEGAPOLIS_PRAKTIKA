import csv  # импортируем библиотеку для работы с csv файлами


with open('space.csv', encoding='utf-8') as file:  # открываем файл для чтения
    reader = list(csv.DictReader(file, delimiter='*', quotechar='"'))  # заносим его строки в список
    hashtab = {}  # создаем хэш таблицу
    for i in range(10):  # первые 10 кораблей
        key = reader[i]['planet']  # создаем ключ
        value = reader[i]['ShipName']  # создаём значение
        hashtab[key] = value  # заносим ключ и значение в хэш таблицу

    print(hashtab)  # вывод хэш таблицы
