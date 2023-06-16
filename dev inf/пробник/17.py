s = open('/home/diana/ЕГЭ/dev inf/пробник/17 (20).txt')
nums = [int(i) for i in s]

mx_2 = 0
for i in nums:
    if 9 < abs(i) < 100:
        mx_2 = max(mx_2, i)
print(mx_2)
k = 0
mx = -10000
for i in range(len(nums) - 1):
    sm = nums[i] + nums[i+1]
    if sm <= mx_2 and (9 < abs(nums[i]) < 100 or 9 < abs(nums[i+1]) < 100):
        k += 1
        mx = max(mx, sm)
print(k, mx)