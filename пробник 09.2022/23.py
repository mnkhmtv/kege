def f(x,s):
    if x == s:
        return 1
    elif x>s:
        return 0
    elif x<s:
        return f(x+3,s) + f(x*2,s)
print(f(3,27)*f(27,63))