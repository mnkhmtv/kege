s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2398.txt')
nums = [int(i) for i in s]

count = mx = 0
for i in range(len(nums) - 2):
    sm = nums[i] + nums[i+1] + nums[i+2]
    if nums[i+1] > 0 and nums[i+1] % 10 == 9:
        if (nums[i] > 0 and nums[i] % 10 == 9) \
            or (nums[i+2] > 0 and nums[i+2] % 10 == 9):
            continue
        count += 1
        mx = max(mx, sm)
print(count, mx)
