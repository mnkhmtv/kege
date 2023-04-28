def pr(x):
    if x == 2:
        return 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1
for i in range(1, 250):
    s = '>' + 16 * '1' + i * '2' + 16 * '3'
    while '>1' in s or '>3' in s or '>2' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>3' in s:
            s = s.replace('>3', '>2', 1)
        if '>2' in s:
            s = s.replace('>2', '>1', 1)
    s = s.replace('>', '0')
    if pr(sum(map(int, s))):
        print(i)
        break