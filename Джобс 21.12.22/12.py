n = []
minn =1e9
for i in range(1, 1000):
    s = 33*'1' + i*'3' + 33*'2'
    while '11' in s or '22' in s or '13' in s or '23' in s:
        s = s.replace('11', '2', 1)
        s = s.replace('22', '1', 1)
        s = s.replace('13', '2', 1)
        s = s.replace('23', '1', 1)
    minn = min(minn, int(s))
    n += [[int(s), i]]
print(n,minn)
for i in n:
    if i[0] == minn:
        print(i[1])
