import sys
input = sys.stdin.readline().strip

n,m = map(int, input().split())

result = 0
if n == 1: result = 1
elif n == 2: result = min((m - 1)//2 + 1, 4)
else:
  if m <= 6 : result = min(m, 4)
  else: result = m - 2

print(result)

