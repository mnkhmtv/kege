# Дана последовательность натуральных чисел. Рассматриваются все её непрерывные
# подпоследовательности, состоящие более чем из ста элементов. Необходимо определить
# количество таких подпоследовательностей, сумма элементов которых кратна 1111.
s = open('/home/diana/ЕГЭ/27/27-B.txt')

n = int(s.readline())
k = 1111
suma = 0
count = 0
sums = []
remains = [1] + [0]*(k-1)

for i in range(n):

    x = int(s.readline())
    suma += x
    sums.append(suma)

    if len(sums) > 100:
        count += remains[suma % k]
        ost = sums.pop(0) % k
        remains[ost] += 1

print(count)