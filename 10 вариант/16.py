def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + 3 * f(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 + 2 * f(n - 2)
print(f(23))