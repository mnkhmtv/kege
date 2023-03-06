def pr(n):
    if n == 2 or n == 1:
        return 1
    pr = 1
    for i in range(2,int(n**0.5)+ 1):
        if n % i == 0:
            pr *= 0
    if pr == 1:
        return 1

ns = []
for n in range(1, 100):
    s = '>' + 16 * '1' + n * '2' + 16 * '3'
    while '>1' in s or '>3' in s or '>2' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>3' in s:
            s = s.replace('>3', '>2', 1)
        if '>2' in s:
            s = s.replace('>2', '>1', 1)
    summ = 0
    for i in s:
        if i == '>':
            summ += 0
        else:
            summ += int(i)
    
    if pr(summ):
        ns += [n]
print(min(ns))
        