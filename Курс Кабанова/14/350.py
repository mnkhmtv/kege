s = '0123456789A'
for x in s:
    left = int('3364' + x, 11) + int(x + '7946', 12)
    right = int('55' + x + '87', 14)
    if left == right:
        print(right)
        break