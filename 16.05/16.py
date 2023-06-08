lst = [0] * 45
for i in range(1, len(lst) - 2):
    if i > 3000:
        lst[i] = i
    elif i <= 3000 and i % 2 == 0:
        lst[i] = i + lst[i + 1] + 1
    elif i <= 3000 and i % 2 != 0:
        lst[i] = lst[i + 2] + 2
print(lst[40] - lst[43])
print(lst[39] - lst[42])