from itertools import product
s = 'abrs'
k = 0
for i1, i2, i3, i4, i5 in product(s, repeat = 5):
    res = i1 + i2 + i3 + i4 + i5
    sog = res.count('r') + res.count('s') + res.count('b')
    k += 1
    if sog <= 3:
        if res.count('a') == 2:
            if res.count('b') == 1 and res.count('r') == 1 and  res.count('s') == 1:
                print(k)
                
        if res.count('b') == 2:
            if res.count('a') == 1 and res.count('r') == 1 and  res.count('s') == 1:
                print(k)
                
        if res.count('r') == 2:
            if res.count('b') == 1 and res.count('a') == 1 and  res.count('s') == 1:
                print(k)
                
        if res.count('s') == 2:
            if res.count('b') == 1 and res.count('r') == 1 and  res.count('a') == 1:
                print(k)
                
