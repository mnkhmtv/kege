n = int(input())
if n <= 0:
    print('Введено некорректное значение')
elif n % 100 == 0 and n % 400 == 0:
    print('Високосный')
elif n % 4 == 0:
    print('Високосный')
else:
    print('Невискосный')
    
def f(n):
    if n <= 0:
        return False
    elif n % 100 == 0 and n % 400 == 0:
        return True
    elif n % 4 == 0:
        return True
    else:
        return False

n = int(input())
print(f(n))