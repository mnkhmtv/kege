# Полина составляет 4-буквенные коды из букв П, О, Л, И, Н, А.
#  Каждую букву можно использовать любое количество раз или совсем не использовать, 
#  при этом нельзя ставить подряд две гласные или две согласные. 
# Сколько различных кодов может составить Полина?
s = 'полина'
k = 0
zap = 'оиа'
zap1 = 'плн'
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                res = i1 + i2 + i3 + i4
                d = 0
                for i in range(len(res)-1):
                    if (res[i] in zap and res[i+1] in zap) or (res[i] in zap1 and res[i+1] in zap1):
                        d +=1
                if d == 0:
                    k+=1
            
print(k)