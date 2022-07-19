import sys


n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

result = 0
for i in range(n-1, -1, -1):
  if k // coin[i] >= 1:
    result += k//coin[i]
    k %= coin[i]
print(result)



