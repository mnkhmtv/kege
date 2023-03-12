s = open('/home/diana/ЕГЭ/СПБ пробник/17.txt')
a = [int(i) for i in s]
max_a = -1e9
for i in a:
    if str(i)[-1] == '5':
        max_a = max(max_a, i)

k = 0
maxx = -1e9
for i in range(len(a) - 1):
    r = abs(a[i]**2 - a[i + 1]**2)
    if (str(a[i])[-1] == '5' and str(a[i + 1])[-1] != '5') or \
          (str(a[i + 1])[-1] == '5' and str(a[i])[-1] != '5'):
        if r < max_a**2:
            k += 1
            maxx = max(r, maxx)
print(k, maxx)