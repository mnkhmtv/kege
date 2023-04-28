def f(n):
    if n < 4:
        return 1
    if n > 3:
        return f(n - 1) * (n - 3)
    
print(f(1401)/f(1397))