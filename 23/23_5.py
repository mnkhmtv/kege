def f(s,x):
    if s>x:
        return 0
    if s == x:
        return 1
    if s<x:
        return f(s+1,x)+f(s*2,x)
print(f(4,22)*f(22,24))