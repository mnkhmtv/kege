s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2017.txt')
nums = [int(i) for i in s]

ans = []

for i in nums:
    s16 = hex(i)[2:]
    if s16[-1] == 'b' and i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
        ans.append(i)

print(len(ans), sum(ans))

