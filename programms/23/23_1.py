def f(s,x):
    if s>x:
        return 0
    if s==x:
        return 1
    if s<x:
        return f(s+1,x)+f(s*3,x)+f(s+2,x)

print(f(2,9)*f(9,11)*f(11,12))