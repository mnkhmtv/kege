# PVPV | + 1 / * 2 | >= 77 | 1)7 2)1<=s<=69

def f(x, y, p):
    if (x + y) >= 77 and p == 3:
        return 1
    if (x + y) < 77 and p == 3:
        return 0
    if (x + y) >= 77 and p < 3:
        return 0