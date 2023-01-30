def f(s,x):
    if s>x or s==10 or s==11:
        return 0
    if s==x:
        return 1
    if s<x:
        return f(s+1,x) + f(s+2,x) + f(s*3,x)
    
    

print(f(8,27)*f(1,8))