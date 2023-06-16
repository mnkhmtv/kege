def sum_divs(x):
    s = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s += i + x // i
    return s

ans = []
for n in range(150_000, 200_000):
    S = sum_divs(n)
    if S % 13 == 10:
        ans.append([n, S])
        if len(ans) > 7:
            break

for i in range(len(ans) - 1):
    print(ans[i][0], ans[i][1])