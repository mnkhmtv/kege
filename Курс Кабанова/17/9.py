s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_1998.txt')
nums = [int(i) for i in s]

count = 0
mn = 1e9

for i in range(len(nums) - 2):
    sr_ar = (nums[i] + nums[i+1] + nums[i+2])// 3
    if abs(nums[i]) % 3 == 0 and abs(nums[i + 1]) % 3 == 0 and abs(nums[i + 2]) % 3 == 0:
        if abs(nums[i]) % 12 == 0 or abs(nums[i + 1]) % 12 == 0 or abs(nums[i + 2]) % 12 == 0:
            count += 1
            mn = min(mn, sr_ar)
print(count, mn)