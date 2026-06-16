x = int(input("Введите ЧЕТЫРХЕЗНАЧНОЕ число:"))
y = x//1000
if 9>= y > 0:
    tisicha = x//1000
    sotka = (x%1000)//100
    desyatka = (x%100)//10
    edinici = x%10
    print(f"Тысяч:{tisicha}")
    print(f"Сотки:{sotka}")
    print(f"Десятки:{desyatka}")
    print(f"Единицы:{edinici}")
else:
    print("Четырехзначное число ввести надо было, тупень")