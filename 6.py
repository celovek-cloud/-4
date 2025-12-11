import  math
x = float(input("Введите число в градусах: "))
math.radians(x)
x = math.sin(x) + math.cos(x) + pow(math.tan(x), 2)
print(x)