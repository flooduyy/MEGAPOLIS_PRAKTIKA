import csv  # импортируем библиотеку для работы с csv файлами


def create_password(s1, s2):  # создаём пароль
    return s1[-3:] + s2[1:3] + s1[0:3][:-1]


space_password = []  # результирующий список
with open('space.csv', encoding='utf-8') as file:  # открываем файл для чтения
    reader = list(csv.DictReader(file, delimiter='*', quotechar='"'))  # заносим его строки в список
    for row in reader:  # вписываем сгенерированный пароль в каждый словать списка
        row['password'] = create_password(row['planet'], row['ShipName'])
        space_password.append(row)  # добавляем словарь с паролем в список

with open('space_uniq_password.csv', 'w', newline='', encoding='utf-8') as file:  # создаем новый файл
    w = csv.DictWriter(file, fieldnames=['ShipName', 'planet', 'coord_place', 'direction', 'password'])
    w.writeheader()
    w.writerows(space_password)  # записываем в него список с паролями
