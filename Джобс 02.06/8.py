from itertools import product
s = '0123456789AB'
k = 0
for i1 in '123456789AB':
    for i2, i3, i4, i5, i6, i7 in product(s, repeat=6):
        
        ans = [int(i1, 12), int(i2, 12), int(i3, 12), int(i4, 12), int(i5, 12), int(i6, 12), int(i7, 12)]
        if (ans[0] % 3 == 0 and ans[1] % 3 != 0 and ans[2] % 3 == 0 and ans[3] % 3 != 0 and \
        ans[4] % 3 == 0 and ans[5] % 3 != 0 and ans[6] % 3 == 0) or \
        (ans[0] % 3 != 0 and ans[1] % 3 == 0 and ans[2] % 3 != 0 and ans[3] % 3 == 0 and \
        ans[4] % 3 != 0 and ans[5] % 3 == 0 and ans[6] % 3 != 0):
            k += 1

print(k)