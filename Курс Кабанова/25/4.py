def sum_div(x):
    sm = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            sm += x // i + i
    return sm

ans = []
for num in range(150_000, 250_000):
    S = sum_div(num)
    if S % 13 == 10:
        if len(ans) <= 7:
            ans += [[num, S]]
        else:
            break

ans.sort()
for i in ans:
    print(*i)