import sys

# 현재 가장 큰 수가 가지고있는 기록보다 그 후에 나온 작은 숫자의 기록은 작을 수 밖에 없기때문에
# 현재의 수만 저장하면 된다.

n = int(sys.stdin.readline().strip())
hanzo = list(map(int, sys.stdin.readline().strip().split()))
maxCount = 0
count = 0
nowNumber = 0
for i in range(n):
  if hanzo[i] > nowNumber: 
    nowNumber = hanzo[i]
    count = 0
  else:
    count += 1
    if maxCount < count: maxCount = count
print(maxCount)
  