# Алгоритм вычисления значений функций F(n), где n  — натуральное число, 
# задан следующими соотношениями:

# F(1) = 1; F(2) = 2; F(3) = 3;

# F(n) = F(n − 3)*n при n >3.

# Чему равно значение функции F(11)? В ответе запишите только натуральное число.

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n>3:
        return f(n-3)*n
print(f(11))