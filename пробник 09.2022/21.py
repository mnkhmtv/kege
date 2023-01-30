# +1 +4 *2 >=165 1<=s<=164
def f(s,p):
    if (p == 2 or p==4) and s>=165:
        return 1
    elif p == 4 and s<165:
        return 0
    elif p<4 and s>=165:
        return 0
    if p%2!=0:
        return f(s+1,p+1) or f(s+4,p+1) or f(s*2,p+1)
    else:
        return f(s+1,p+1) and f(s+4,p+1) and f(s*2,p+1)

for s in range(1,165):
    if f(s,0)==1:
        print(s)

def f1(s,p):
    if p == 2 and s>=165:
        return 1
    elif p == 2 and s<165:
        return 0
    elif p==1 and s>=165:
        return 0
    if p%2!=0:
        return f1(s+1,p+1) or f1(s+4,p+1) or f1(s*2,p+1)
    else:
        return f1(s+1,p+1) and f1(s+4,p+1) and f1(s*2,p+1)
for s in range(1,165):
    if f1(s,0)==1:
        print(s)