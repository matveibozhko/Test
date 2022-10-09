# выводим и счетаем чек с налогом и чаевыми
check = float(input("введите сумму счета"))
tips = check * 0.18
tax = (check + tips) * 0.2
summa = check + tax + tips
tips = '%.2f' % tips
tax = '%.2f' % tax
summa = '%.2f' %summa
print(f" общая сумма : {summa} \n налог : {tax} \n чаевый : {tips}")