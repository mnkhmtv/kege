# Автомат получает на вход четырёхзначное число 
# (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.

# 1.  Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.

# 2.  Наименьшая из полученных трёх сумм удаляется.

# 3.  Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей
# Укажите наибольшее число, при обработке которого автомат выдаёт результат 1315
s = '0123456789'
s1 = '123456789'
maxx = 0

for i1 in s1:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                a = []
                res = i1 + i2 + i3 + i4
                a+=[int(i1)+int(i2)] 
                a+=[int(i2)+int(i3)]
                a+=[int(i3)+int(i4)]
                a.sort()
                a.pop(0)
                ress = str(a[0]) + str(a[1])
                if ress == '1315':
                    if int(res)>maxx:
                        maxx = int(res)
print(maxx)



