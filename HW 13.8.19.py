b = int(input('введите количество билетов\t'))
spisok_1 = []
i = 0
while i < b:
    x = int(input('введите возраст посетителя\t'))
    if 0 < x < 18:
        spisok_1.append(0)

    if 18 <= x < 25:
        spisok_1.append(990)

    if x >= 25:
        spisok_1.append(1390)

    i = i + 1

y = sum(spisok_1)
cena = 0
if b > 3:
    cena = y*9/10
else:
    cena = y
print(cena)
