def f(n):
    if n <= 1:
        return -1
    if n > 1 and n % 2 == 0:
        return (2*n - 3) * f(n -1)
    if n > 1 and n % 2 != 0:
        return n ** 2 - n + f(n - 1)

print(f(11))