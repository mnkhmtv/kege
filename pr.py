x1, y1, x2, y2 = map(int, input().split())
'''
shir1 = len1 = shir2 = len2 = 0
if x1 < y1:
	shir1, len1 = x1, y1
else:
	shir1, len1 = y1, x1

if x2 < y2:
	shir2, len2 = x2, y2
else:
	shir2, len2 = y2, x2
'''
a = [x1 + x2, y1 +y2, x1 + y2, x2 + y1, x1 + y1, x2 + y2]
s1 = x1 * y1
s2 = y2 * x2
k1 = k2 = 0
for i in range(min(a), max(a)):
    for j in range(min(a), max(a)):
        if i * j >= (s1 + s2):
            k1 = i
            k2 = j
            break
    if k1 != 0 and k2 != 0:
        break
    
print(k1, k2)
