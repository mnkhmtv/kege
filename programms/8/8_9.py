# Шифр кодового замка представляет собой последовательность из пяти символов,
#  каждый из которых является цифрой от 1 до 5. Сколько различных вариантов шифра 
#  можно задать, если известно, что цифра 1 встречается ровно три раза, 
#  а каждая из других допустимых цифр может встречаться в шифре 
# любое количество раз или не встречаться совсем?
s = '12345'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    res = i1 + i2 + i3 + i4 + i5
                    if res.count('1') == 3:
                        k+=1
print(k)