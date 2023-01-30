# Настя составляет 4-буквенные коды из букв Н, А, С, Т, Я. Каждую букву можно использовать не более одного раза, 
# при этом нельзя ставить рядом две гласные и две согласные. Сколько различных кодов может составить Настя?

letters = 'настя'
k = 0
for i1 in letters:
    for i2 in letters:
        for i3 in letters:
            for i4 in letters:
                s = i1+i2+i3+i4
                if s.count('н') == 1 and s.count('а') == 1 and s.count('с') == 1 and s.count('т') == 1 and s.count('я') == 1:
                    if 'аа' not in s and 'яя' not in s and 'нн' not in s and 'сс' not in s and 'тт' not in s and 'ая' not in s and 'яа' not in s and 'нт' not in s and 'нс' not in s and 'сн' not in s and 'ст' not in s and 'тс' not in s and 'тн':
                        k+=1
print(k)