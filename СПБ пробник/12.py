def dell(n):
    k = 0
    for i in range(2, int(n**0.5) + 1):
        if n**0.5 == i:
            k += 1
            continue
        elif n % i == 0:
            k += 2
    if k == 3:
        return 1
    
for i in range(1, 1000):
    s = '>' + 15 * '1' + 35 * '2' + i * '3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '3>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>', 1)
    summ = 0
    for j in s:
        if j != '>':
            summ += int(j)
    if dell(summ):
        print(i)
        input()
 