def deliteli(n):
    k = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            k += 2
    return k

count = 0
suma = 0
def summ(n):
    return sum([int(i) for i in str(n)])

for i in range(51242, 421421 + 1):
    if i % summ(i) == 0 and deliteli(i) == 6:
        count += 1
        suma += i

print(count, suma/count)
