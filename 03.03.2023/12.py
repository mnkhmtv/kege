need = []
minn = 1e9
for n in range(301, 1000):
    s = n * '2'
    while '222222' in s:
        s = s.replace('222222', '3333', 1)
        s = s.replace('3333', '2222', 1)
    minn = min(minn, s.count('2'))
    need += [[n, s.count('2')]]
print(minn)
need.sort()
for i in need:
    if i[1] == minn:
        print(i[0])
