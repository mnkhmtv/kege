count = 0
for i in range(100_000_023, 999_999_987):
    s = str(i)
    if s.count('0') < 7:
        a = []
        for i in s:
            a.append(int(i))
        se = set(a)
        if len(se) >= 3:
            count +=1
print(count)