for n in range(6, 36):
    if (7 ** 500  - int('53', n)) % 6 == 0:
        print(n)
        break
