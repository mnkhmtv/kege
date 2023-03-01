#+10/*2 >=82 1<=s<=81

def f(x, p):
    if (p == 1 and x < 82) and (x * 2 >= 82 or x + 10 >= 82):
        return 1
    elif p == 1 and x >= 82:
        return 0
    
    return f(x + 10, p + 1) or f(x * 2, p +1)
    

for s in range(1, 82):
    if f(s,0):
        print(s)