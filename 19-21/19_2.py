# >=93 1)12 2) 1<=s<=80 +1 *2

# Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. 
# Укажите минимальное значение S, когда такая ситуация возможна

def f(x,y,p):
    if x+y>=93 and p==2:
        return 1
    elif x+y<93 and p==2:
        return 0
    elif p<2 and x+y>=93:
        return 0
    return f(x,y+1,p+1) or f(x,y*2,p+1) or f(x+1,y,p+1) or f(x*2,y,p+1)

for s in range(1,81):
    if f(12,s,0):
        print(s)