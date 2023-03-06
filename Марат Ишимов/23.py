# -4 -sum(n)  36 -> 2 (14)
def ssum(n):
    s = str(n)
    summ = 0
    for i in s:
        summ += int(i)
    return summ
    
def f(x, s):
    if x < s:
        return 0
    if x == s:
        return 1
    if x > s:
        return f(x - 4, s) + f(x - ssum(x), s)

print(f(36,14)*f(14,2))