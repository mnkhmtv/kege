s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2403.txt')
nums = [int(i) for i in s]

mx = count = 0
for i in range(len(nums) - 1):
    if (abs(nums[i]) % 8 == 3 and abs(nums[i+1]) % 9 == 0 and abs(nums[i]) % 9 != 0) or \
        (abs(nums[i + 1]) % 8 == 3 and abs(nums[i]) % 9 == 0 and abs(nums[i+1]) % 9 != 0):
        count += 1
        mx = max(mx, nums[i], nums[i+1])
print(count, mx)