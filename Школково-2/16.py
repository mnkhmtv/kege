def f(n):
    if n < 12:
        return n
    if n > 11 and n % 2 == 0:
        return g(n//2) * 2 - f(n - 1)
    if n > 11 and n % 2 == 1:
        return g(n - 1) * (-1)

def g(n):
    if n < 12 and n % 3 != 0:
        return f(n-1) + n
    if n < 12 and n % 3 == 0:
        return g(n - 1) + f(n // 3) - n
    return n * n

def s(n):
    return sum([int(i) for i in str(abs(n))])

for i in range(1, 1000 + 1):
    if s(f(i)) == 33:
        print(i)
