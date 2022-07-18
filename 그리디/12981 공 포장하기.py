nums = list(map(int, input().split()))
m = min(nums)
result = m
for i in range(len(nums)): 
  nums[i] -= m
  result += nums[i]//3
  nums[i] %= 3
if sum(nums) == 0: result +=0
elif sum(nums) <= 2: result += 1
else: result += 2

print(result)
