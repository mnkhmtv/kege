#PVPV | + 2/ * 2 | >= 118 | 1)3 2)1 <= s <= 113

def f19(x, y, p):
    if (x + y) >= 118 and p == 2:
        return 1
    if (x + y) < 118 and p == 2:
        return 0
    if (x + y) >= 118 and p < 2:
        return 0
    
    return f19(x + 2, y, p + 1) or f19(x * 2, y, p + 1) or \
    f19(x, y + 2, p + 1) or f19(x, y * 2, p + 1)

# for s in range(1, 114):
#     if f19(3, s, 0):
#         print(s)
#         break


def f20(x, y, p):
    if (x + y) >= 118 and p == 3:
        return 1
    if (x + y) < 118 and p == 3:
        return 0
    if (x + y) >= 118 and p < 3:
        return 0
    
    if p % 2 == 0:
        return f20(x + 2, y, p + 1) or f20(x * 2, y, p + 1) or \
        f20(x, y + 2, p + 1) or f20(x, y * 2, p + 1)
    else:
        return f20(x + 2, y, p + 1) and f20(x * 2, y, p + 1) and \
        f20(x, y + 2, p + 1) and f20(x, y * 2, p + 1)
# k = 0
# for s in range(1, 114):
#     if f20(3, s, 0):
#         k += 1
#         if k == 1 or k == 2:
#             print(s)

def f21(x, y, p):
    if (x + y) >= 118 and (p == 2 or p == 4):
        return 1
    if (x + y) < 118 and p == 4:
        return 0
    if (x + y) >= 118 and p < 4:
        return 0
    if p % 2 != 0:
        return f21(x + 2, y, p + 1) or f21(x * 2, y, p + 1) or \
        f21(x, y + 2, p + 1) or f21(x, y * 2, p + 1)
    else:
        return f21(x + 2, y, p + 1) and f21(x * 2, y, p + 1) and \
        f21(x, y + 2, p + 1) and f21(x, y * 2, p + 1)

for s in range(1, 114):
    if f21(3, s, 0):
        print(s)

print('-------')

def f211(x, y, p):
    if (x + y) >= 118 and p == 2:
        return 1
    if (x + y) < 118 and p == 2:
        return 0
    if (x + y) >= 118 and p < 2:
        return 0
    if p % 2 != 0:
        return f211(x + 2, y, p + 1) or f211(x * 2, y, p + 1) or \
        f211(x, y + 2, p + 1) or f211(x, y * 2, p + 1)
    else:
        return f211(x + 2, y, p + 1) and f211(x * 2, y, p + 1) and \
        f211(x, y + 2, p + 1) and f211(x, y * 2, p + 1)

for s in range(1, 114):
    if f211(3, s, 0):
        print(s)