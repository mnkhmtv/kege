# Последовательность чисел Падована задается рекуррентным соотношением:

# F(1) = 1

# F(2) = 1

# F(3) = 1

# F(n) = F(n–3) + F(n–2), при n >3, где n – натуральное число.

# Чему равно десятое число в последовательности Падована?

# В ответе запишите только натуральное число.

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    elif n>3: 
        return f(n-3) + f(n-2) 

print(f(10))