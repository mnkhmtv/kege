# >=45 s=4 1<=s<=40 +1 *3 
def f(x,y,p):
    if (p==2 or p==4) and y+x>=45:
        return 1
    elif p==4 and y+x<45:
        return 0
    elif y+x>=45:
        return 0
    if p%2!=0:
        return f(x+1,y,p+1) or f(x*3,y,p+1) or f(x,y*3,p+1) or f(x,y+1,p+1)
    else:
        return f(x+1,y,p+1) and f(x*3,y,p+1) and f(x,y*3,p+1) and f(x,y+1,p+1)

for s in range(1,41):
    if f(4,s,0)==1:
        print(s)    

print('----')

def f1(x,y,p):
    if p==2 and y+x>=45:
        return 1
    elif p==2 and y+x<45:
        return 0
    elif y+x>=45:
        return 0
    if p%2!=0:
        return f1(x+1,y,p+1) or f1(x*3,y,p+1) or f1(x,y*3,p+1) or f1(x,y+1,p+1)
    else:
        return f1(x+1,y,p+1) and f1(x*3,y,p+1) and f1(x,y*3,p+1) and f1(x,y+1,p+1)

for s in range(1,41):
    if f1(4,s,0)==1:
        print(s)