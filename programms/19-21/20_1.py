# >=45 s=4 1<=s<=40 +1 *3 
def f(x,y,p):
    if p==3 and y+x>=45:
        return 1
    elif p==3 and y+x<45:
        return 0
    elif p!=3 and y+x>=45:
        return 0
    if p%2==0:
        return f(x+1,y,p+1) or f(x*3,y,p+1) or f(x,y*3,p+1) or f(x,y+1,p+1)
    else:
        return f(x+1,y,p+1) and f(x*3,y,p+1) and f(x,y*3,p+1) and f(x,y+1,p+1)

for s in range(1,41):
    if f(4,s,0)==1:
        print(s)
        