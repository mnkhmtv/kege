# В файле содержится последовательность из 10 000 целых положительных чисел.
#  Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар 
#  элементов последовательности, у которых сумма элементов кратна 60 и 
#  хотя бы один элемент из пары делится на 40, затем максимальную из сумм элементов таких пар.
#   В данной задаче под парой подразумевается два различных элемента последовательности.
#  Порядок элементов в паре не важен.
a = open('/home/diana/ЕГЭ/17/17 (4).txt')

count = 0
m = 0
l = [int(i) for i in a]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] + l[j]) % 60 == 0 and (l[i] % 40 == 0 or l[j] % 40 == 0):
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)