n = int(input())
rate = [int(input()) for _ in range(n)]

result = 0
for i in range(n-1, 0, -1):
  if rate[i] <= rate[i-1]:
    result += rate[i-1] - rate[i] + 1
    rate[i-1] -= rate[i-1] - rate[i] + 1
print(result)
  