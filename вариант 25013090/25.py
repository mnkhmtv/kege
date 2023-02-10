n1 = 135790
n2 = 163228

def f(n):
    dels = []
    summ = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.append(i)
            dels.append(n // i)
            summ += (i + n // i)

    if summ > 460_000:
        return len(dels), summ

for i in range(n1, n2 + 1):
    if f(i) != None:
        print(f(i))