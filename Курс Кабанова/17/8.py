s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_1998.txt')
nums = [int(i) for i in s]
count = 0
mx = -100000
for i in range(len(nums) - 2):
    summ = nums[i] + nums[i+1] + nums[i+2]
    pr = nums[i] * nums[i+1] * nums[i+2]
    if pr % 7 == 0 and summ % 10 == 5:
        count += 1
        mx = max(mx, summ)
print(count, mx)