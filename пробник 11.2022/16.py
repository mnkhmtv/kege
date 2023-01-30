import sys
sys.setrecursionlimit(10000)

def f(n):
    if n>=10000:
        return n
    elif n<10000 and n%2==0:
        return f(n+2)-3
    elif n<10000 and n%2!=0:
        return f(n+2)+1

print(f(94)-f(80))