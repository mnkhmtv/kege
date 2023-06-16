f = open('/home/diana/ЕГЭ/programms/26/26_33.txt')
s, n = map(int, f.readline().split())
print(s,n)
a = [int(i) for i in f]
a.sort()

sm_now = ans1 = 0
for i in range(n):
    if sm_now + a[i] <= s:
        sm_now += a[i]
        ans1 += 1
    else:
        break

sm_now -= a[ans1 - 1]
ans2 = 0

for i in range(ans1, n):
    if sm_now + a[i] <= s:
        ans2 = a[i]
    else:
        break

print(ans1, ans2, sm_now + ans2)