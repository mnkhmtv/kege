#PVPV | +1/+4/*4 | >= 78 | 1 <= s <= 77
# 19
def f(x, p):
    if p == 2 and x >= 78:
        return 1
    if p == 2 and x < 78:
        return 0
    if p < 2 and x >= 78:
        return 0
    
    if p % 2 != 0:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 4, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 4, p + 1)

# for s in range(1, 78):
#     if f(s, 0): print(s)
# 20
# def f1(x, p):
#     if (p == 1 or p == 3) and x >= 78:
#         return 1
#     if p == 3 and x < 78:
#         return 0
#     if p < 3 and x >= 78:
#         return 0
    
#     if p % 2 == 0:
#         return f1(x + 1, p + 1) or f1(x + 4, p + 1) or f1(x * 4, p + 1)
#     else:
#         return f1(x + 1, p + 1) and f1(x + 4, p + 1) and f1(x * 4, p + 1)

# for s in range(1, 78):
#     if f1(s, 0): print(s)
# print('-----')
# def f12(x, p):
#     if p == 1 and x >= 78:
#         return 1
#     if p == 1 and x < 78:
#         return 0
#     if p < 1 and x >= 78:
#         return 0
    
#     if p % 2 == 0:
#         return f12(x + 1, p + 1) or f12(x + 4, p + 1) or f12(x * 4, p + 1)
#     else:
#         return f12(x + 1, p + 1) and f12(x + 4, p + 1) and f12(x * 4, p + 1)

# for s in range(1, 78):
#     if f12(s, 0): print(s)

def f1(x, p):
    if (p == 2 or p == 4) and x >= 78:
        return 1
    if p == 4 and x < 78:
        return 0
    if p < 4 and x >= 78:
        return 0
    
    if p % 2 != 0:
        return f1(x + 1, p + 1) or f1(x + 4, p + 1) or f1(x * 4, p + 1)
    else:
        return f1(x + 1, p + 1) and f1(x + 4, p + 1) and f1(x * 4, p + 1)

for s in range(1, 78):
    if f1(s, 0): print(s)
print('-----')

def f12(x, p):
    if p == 2 and x >= 78:
        return 1
    if p == 2 and x < 78:
        return 0
    if p < 2 and x >= 78:
        return 0
    
    if p % 2 != 0:
        return f12(x + 1, p + 1) or f12(x + 4, p + 1) or f12(x * 4, p + 1)
    else:
        return f12(x + 1, p + 1) and f12(x + 4, p + 1) and f12(x * 4, p + 1)

for s in range(1, 78):
    if f12(s, 0): print(s)