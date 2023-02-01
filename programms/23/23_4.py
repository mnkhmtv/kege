def f(s,x):
    if s>x or s == 25:
        return 0
    if s == x:
        return 1
    if s<x:
        return f(s+1,x)+f(s*2,x)

print(f(2,14)*f(14,29))