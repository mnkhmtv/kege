# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:

# 1. ААААА

# 2. ААААО

# 3. ААААУ

# 4. АААОА

# Укажите номер слова ОАОАО.

s = 'аоу'
k=0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    res = i1 + i2 + i3 +i4 +i5
                    k+=1
                    if res == 'оаоао':
                        print(k)