a = int(input())
b = int(input())
c = int(input())
'''
if c < 0:
    print('NO SOLUTION')
else:
    if a == 0 and b >= 0 and b == c**2:
        print('MANY SOLUTIONS')
    elif a == 0 and c**2 - b != 0:
        print('NO SOLUTIONS')
    if a != 0:
        x = (c**2 - b)%a
        if x == 0:
            print((c**2 - b)//a)
'''
if c < 0 or (a == 0 and c**2 - b != 0):
    print('NO SOLUTION')
elif a == 0 and c**2 == b:
    print('MANY SOLUTIONS')
elif (c**2 - b)%a == 0:
    print((c**2 - b)//a)
else:
    print('NO SOLUTION')
