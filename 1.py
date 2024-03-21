import csv  # импортируем библиотеку для работы с csv файлами


with open('space.csv', encoding='utf-8') as file:  # открываем файл для чтения
    reader = list(csv.reader(file, delimiter='*'))[1:]  # заносим все его строки в список
    for ShipName, planet, coord_place, direction in reader:  # пробегаемся по каждой строчке
        s = ShipName.split('-')
        n = int(s[1][0])  # задаём нужные значения
        m = int(s[1][1])
        t = len(planet)
        xd, yd = map(int, direction.split())
        if '0 0' in coord_place:  # если координаты нулевые
            if n > 5:  # составляем новые координаты по формуле
                x = n + xd
            else:
                x = -4*(n+xd) + t
            if m > 3:
                y = m + t + yd
            else:
                y = -m * (n + yd)
        if s[0][-1] == 'V':  # если нашли нужный код
            print(f"{ShipName}-{x},{y}")  # выводим согласно формуле

    for el in reader:  # меняем нулевые координаты
        if el[-2] == '0 0':
            el[-2] = f"{x} {y}"


with open('space_new.txt', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)  # заносим новый список в файл
    w.writerow(['ShipName', 'planet', 'coord_place', 'direction'])
    w.writerows(reader)
