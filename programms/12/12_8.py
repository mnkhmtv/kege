def pr(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
k = 0
for i in range(10,100):
    s = '1' + i*'0'
    while '10' in s:
        if '10' in s:
            s = s.replace('10','001',1)
        if '1' in s:
            s = s.replace('1','01')
    if pr(len(s)):
        k+=1
print(k)
