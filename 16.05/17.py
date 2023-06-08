s = open('/home/diana/ЕГЭ/16.05/17 (18).txt')
a = [int(i) for i in s]

def three(x):
    return 100 <= abs(x) <= 999

def max_three(a : list):
    mx = -1e9
    for i in a:
        if three(i):
            mx = max(mx, i)
    return mx

def countt(a : list):
    count = 0
    max_summ = -1e9
    mx = max_three(a)
    for i in range(len(a) - 1):
        summ = a[i] + a[i + 1]
        if ((three(a[i]) == 0 and three(a[i + 1]) == 1) \
            or (three(a[i + 1]) == 0 and three(a[i]) == 1)):
            if summ <= mx:
                count += 1
                max_summ = max(max_summ, summ)
    return (count, max_summ)

print(countt(a))