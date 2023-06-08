s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_1993.txt')
nums = [int(i) for i in s]

mx = count = 0
for i in range(len(nums) - 1):
    sump = nums[i] + nums[i + 1]
    pr = nums[i] * nums[i + 1]
    if abs(sump) % 3 == 0 and abs(sump) % 6 != 0 and abs(pr) % 10 == 8:
        count += 1
        mx = max(mx, sump)
print(count, mx)
