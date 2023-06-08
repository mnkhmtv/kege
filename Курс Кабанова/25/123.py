def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def divid(n):
        deviders = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i not in deviders and prime(i):
                    deviders.append(i)
                if n // i not in deviders and prime(n // i):
                    deviders.append(n // i)
        return deviders

ans = []
for i in range(416782, 498325):

    deviders = divid(i)

    if len(deviders) >= 3 and deviders[0] % 10 == deviders[1] % 10 == deviders[2] % 10 \
          and (deviders[0] * deviders[1] * deviders[2]) == i:
        ans.append(i)

print(len(ans), max(ans) - min(ans))

