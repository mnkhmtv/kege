minn = []
for n in range(100, 1000):
    s = n * '3'
    while '111' in s or '333' in s:

        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)

    minn += [[n, int(s)]]

mmin = 1e9
for i in minn:
    mmin = min(i[1], mmin)

print(minn)