def divid(n):

    deviders = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            deviders.add(i)
            deviders.add(n // i)

    return len(deviders)

prev_k = -1
seq = []

for i in range(700_000, 1_000_000):

    cur_k = divid(i)

    if cur_k > prev_k:
        seq += [[i, cur_k]]
        prev_k = cur_k
        
    if len(seq) == 5:
        break

for i in seq:
    print(*i)





