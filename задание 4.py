#вычесляем площадь правильного мнгоугольника
a = int(input("введите длинну стороны в правильном мнгоугольнике: "))
n = int(input("введите количество сторон в правильном мнгоугольнике: "))
t = import.math.tan(a)
s = (n * a**2) / (4 * t * (180 / n))
print(s)