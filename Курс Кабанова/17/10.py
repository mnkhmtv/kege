s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2402.txt')
nums = [int(i) for i in s]

def s3(x):
    ss = ''
    while x > 0:
        ss += str(x % 3)
        x //= 3
    return int(ss[0])
    
count = summ = 0
for i in range(len(nums) - 2):
    if s3(nums[i]) == 2 or s3(nums[i+1]) == 2 or s3(nums[i+2]) == 2:
        count += 1
        summ += min(nums[i], nums[i+1], nums[i+2])
print(count, summ)


