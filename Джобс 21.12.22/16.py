import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 2
    return f(n-1) * ((3**(n%5))//3**(n%7))
    
print(f(1025))
print(f(1030))