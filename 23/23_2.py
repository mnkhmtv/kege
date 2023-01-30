def f(s,x):
    if s>x or s==24:
        return 0
    if s==x:
        return 1
    if s<x:
        return f(s+1,x)+f(2*s+1,x)
print(f(1,25))