s1 =[str(i) for i in range (100)]
s1 += ['']
s2 = [str(i) for i in range(10)]
need = []
for x in s2:
    for y in s2:
        for z in s1:
            r = int('671' + x + y + '1' + z)
            if r % 2023 == 0:
                need += [[r, r//2023]]
need.sort()
for i in need:
    print(*i)