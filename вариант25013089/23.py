# + 1 / * 2 / **2
def f(x, s):

    if x > s:
        return 0
        
    elif x == s:
        return 1

    elif x < s:
        return f(x + 1, s) + f(x * 2, s) + f(x**2, s)

print(f(5,154))
