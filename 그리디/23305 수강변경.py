n = int(input())

data = list(map(int, input().split()))
a = [0] * 1000001
for d in data: a[d] += 1

data = list(map(int, input().split()))
result = 0
for d in data: 
  if a[d] > 0: a[d] -= 1
  else: result += 1

print(result)