s = 120 * '8'
while '888' in s or '2222' in s:
    if '2222' in s:
        s = s.replace('2222', '88', 1)
    else:
        s = s.replace('888', '22', 1)

print(s.count('8'))