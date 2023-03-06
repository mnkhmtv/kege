s = open('/home/diana/ЕГЭ/Марат Ишимов/17_5635.txt')
a = [int(i) for i in s]

need = []
for i in a:
    n = str(abs(i))
    if abs(i) > 30: 
        if n[-2] + n[-1] == '31': need += [i]
print(need)
main_sum = min(need) + max(need)
# print(main_sum)
count = 0
max_sum = -1e9
for i in range(0, len(a) - 1):
    summ = a[i] + a[i + 1]
    if a[i] > main_sum and a[i + 1] > main_sum:
        count += 1
        max_sum = max(max_sum, summ)
print(count, max_sum)
 