s = 3 * (1024 ** 75) + 2 * (256 ** 76) - 16 ** 77 - 2023
n = int(str(s), 32)
print(str(n).count('0'))
print(n)
n = ''
s = 3 * (1024 ** 75) + 2 * (256 ** 76) - 16 ** 77 - 2023
while s > 0:
    n += str(s % 32)
    s //= 32

print(n.count('0'))
print(n)
print('----')
s = 3 * (1024 ** 75) + 2 * (256 ** 76) - 16 ** 77 - 2023

s = '000000000000000000000000000000'
print(len(s))