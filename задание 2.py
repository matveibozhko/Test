#узнаем площадь и переводим в акры
long = int(input("введите длинну участка в фунтах "))
width = int(input("введите ширину участка в фунтах"))
area = float(( long * width) / 43560)
print(area)