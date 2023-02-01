max_ = 1
for i in range(1000,10000):
    s = str(i)
    s1 = int(s[0])
    s2 = int(s[1])
    s3 = int(s[2])
    s4 = int(s[3])
    res1 = s1*s2
    res2 = s3*s4
    if res1<res2:
        res = str(res1)+str(res2)
    elif res1==res2:
        res = str(res1)+str(res2)
    else:
        res = str(res2)+str(res1)
    if res == '1214':
        print(i)
    if int(res)>max_:
        max_ = int(res)
# print(max_)