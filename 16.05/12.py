def f(s):
        while '12' in s or '233' in s or '3333' in s:
            if '12' in s:
                s = s.replace('12', '332', 1)
            if '233' in s:
                s = s.replace('233', '23', 1)
            if '3333' in s:
                s = s.replace('3333', '32', 1)
        return (sum(map(int, s))) % 6

for n in range(6, 100):
    s = '1' + n * '3'
    if f(s) == 0:
        print(n)
        break