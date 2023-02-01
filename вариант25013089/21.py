# *2 / *3  >= 100  1 <= s <= 99
def f(x,p):

    if (p == 2 or p ==4) and x >= 100:
        return 1
    elif p == 4 and x <= 100:
        return 0
    elif p < 4 and x >= 100:
        return 0

    if p % 2 != 0:
        return f(x * 2, p + 1) or f(x * 3, p + 1)
    else: 
        return f(x * 2, p + 1) and f(x * 3, p + 1)

for s in range(1, 100):
    if f(s, 0):
        print(s)

print('---------')

def f1(x,p):

    if p ==2 and x >= 100:
        return 1
    elif p == 2 and x <= 100:
        return 0
    elif p < 2 and x >= 100:
        return 0

    if p % 2 != 0:
        return f1(x * 2, p + 1) or f1(x * 3, p + 1)
    else: 
        return f1(x * 2, p + 1) and f1(x * 3, p + 1)

for s in range(1, 100):
    if f1(s, 0):
        print(s)