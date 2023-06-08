s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2003.txt')
nums = [int(i) for i in s]
count = mx = 0
for i in range(len(nums)):
    if nums[i] % 3 == 0 and nums[i] % 7 != 0 and nums[i] % 17 != 0 and \
        nums[i] % 19 != 0 and nums[i] % 27 != 0:
        count += 1
        mx = max(mx, nums[i])
print(count, mx)