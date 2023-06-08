s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2400.txt')
nums = [int(i) for i in s]

count = 0
mx = -1e9

for i in range(len(nums) - 1):
    sm = nums[i] + nums[i+1]
    pr = nums[i] * nums[i+1]
    if sm >= 100 and (pr < 0 or (nums[i] < 0 and nums[i+1] < 0)):
        count += 1
        mx = max(mx, pr)

print(count, mx)