s = 49**7 + 7**21 - 7

s1 = ''

while s > 0:
    s1 += str(s%7)
    s //= 7

print(s1.count('6'))