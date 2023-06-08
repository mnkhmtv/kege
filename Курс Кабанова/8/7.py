from itertools import product

k = 0
s = 'abikolyn'

sog = 'bkln'
gl = 'aioy'
nt = []
for i in sog:
      for j in sog:
            nt.append(i + j)    
for i in gl:
      for j in gl:
            nt.append(i + j)    

for i1, i2, i3, i4, i5, i6, i7, i8 in product(s, repeat = 8):
    res = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8

    if res.count('a') == 1 and res.count('b') == 1 and res.count('i') == 1 and \
    res.count('k') == 1 and res.count('o') == 1 and res.count('l') == 1 and \
    res.count('y') == 1 and res.count('n') == 1:
        
        flag = 1
        for i in nt:
            if i in res:
                 flag = 0
                 break
            
        if flag == 1:
            k += 1

print(k)
    