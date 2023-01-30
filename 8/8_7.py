# Света составляет 5-буквенные коды из букв С, В, Е, Т, А. 
# Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные. 
# Сколько различных кодов может составить Света?
s = 'света'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    res = i1 + i2 +i3 + i4 + i5
                    if res.count('с')==1 and res.count('в')==1 and res.count('е')==1 and res.count('т')==1 and res.count('а')==1 and ('ае' not in res) and ('еа' not in res):
                        
                        k+=1
print(k)